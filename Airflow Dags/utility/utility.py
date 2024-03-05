 
import datetime
from .database_helper import database_helper,snowflake_helper
import pandas as pd
import os
import json


def get_lastextract_snowflake(table_name,database='amazonebooks',warehouse='COMPUTE_WH'):

    snowflake_db = snowflake_helper({'database_name' : database,'warehouse' : warehouse})

    snow_query = f'''Select last_extract_date from config.table_config  where table_name = '{table_name}';'''

    snow_df = snowflake_db.query_exec_getresult(snow_query)
    snowflake_db.connection_close()

    return snow_df

def get_currentdate_extract_mysql(last_extract_date_df, table_name, database='amazonebooks'):
    if last_extract_date_df.empty:
        query = f"Select distinct business_date as business_date from {database}.{table_name}"

    else:
        print(last_extract_date_df)
        last_extract_date_obj = last_extract_date_df['LAST_EXTRACT_DATE'][0]

        query = f'''Select distinct business_date from {database}.{table_name} where business_date > '{last_extract_date_obj}';'''

    db = database_helper('amazonebooks')
    df = db.query_exec_getresult(query)

    current_extract_date_objs = df["business_date"]
    db.connection_close()

    return current_extract_date_objs

def download_data_local(data):

    database_name = data.get("database_name","")
    table_name = data.get("table_name","")
    current_extract_date_objs = data.get("current_extract_date_objs","")
    const_outdir_path = data.get("outdir_path","")

    db = database_helper(database_name)
    data_location = {}
    for date in current_extract_date_objs:

        query = f'''Select * from {database_name}.{table_name} where business_date = '{date}';'''
        df = db.query_exec_getresult(query)

        date_string = f'''{date.strftime('%Y')}{date.strftime('%m')}{date.strftime('%d')}'''

        outdir_path = f'{const_outdir_path}{database_name}/{table_name}/{date_string}'
        filename = f'{date_string}-{table_name.replace("_","-")}.csv'

        # If Directory is not present then create it.
        if not os.path.exists(outdir_path):
            os.mkdir(outdir_path)

        absolute_path = os.path.join(outdir_path, filename)
        df.to_csv(absolute_path,sep=',',index=False, encoding='utf-8')

        data_location[str(date)] = f'{outdir_path}/{filename}'

    db.connection_close()
    return data_location

def load_data_to_snowsql_stage(data):

    database_name = data.get("database_name","")
    warehouse = data.get("warehouse","COMPUTE_WH")
    schema = data.get("schema","PUBLIC")
    table_name = data.get("table_name", None)
    data_location_dict = data.get("data_location_dict", None)
    stage_table = data.get("stage_table",f'{table_name}_stage' )

    snowflake_db = snowflake_helper({'database_name' : database_name,'warehouse' : warehouse,'schema': schema})

    for path in data_location_dict.values():
        # Note Schema  needs to be selected to execute the below query , in the Code By default schema is Public
        query=f'''PUT 'file:////{path}' @{stage_table};'''
        snowflake_db.query_exec(query)

    snowflake_db.connection_close()

def load_stage_to_snowsql_table(data):
    database_name = data.get("database_name","")
    warehouse = data.get("warehouse","COMPUTE_WH")
    schema = data.get("schema","PUBLIC")
    table_name = data.get("table_name", None)
    stage_table = data.get("stage_table",f'{table_name}_stage' )
    load_type = data.get("load_type",'Snapshot')

    snowflake_db = snowflake_helper({'database_name' : database_name,'warehouse' : warehouse,'schema': schema})

    if load_type == 'Incremental':

        query = 'USE SCHEMA CONFIG;'
        snowflake_db.query_exec(query)
        query = f"SELECT * FROM tbl_primary_key where table_name = '{table_name}';"
        primary_key_data_df =  snowflake_db.query_exec_getresult(query)

        query = f'USE SCHEMA {schema};'
        snowflake_db.query_exec(query)

        # The Below Code generates a Delete Query before the Copy the Data to table
        # by fetching all primary keys
        # Note in snowflake we cannot use delete and Join togather insted we can use 'USING'
        # example as shown below

        '''
        DELETE FROM  amazone_books T1
        USING ( SELECT  t.$1 as col1 FROM @amazone_books_stage t) T2
        WHERE  T1.book_id = T2.col1 ;
        '''

        query = f'DELETE FROM  {table_name} T1 USING ( SELECT '
        query_part1 = ''
        query_part2 = ''
        query_part3 = ''


        for i in range(primary_key_data_df.shape[0]):

            stage_position = (primary_key_data_df.loc[i,["STAGE_POSITION"]]).item()
            primary_column = (primary_key_data_df.loc[i,["PRIMARY_COLUMN"]]).item()

            query_part1 += f' t.${stage_position} as col{stage_position},'
            query_part2 += f' T1.{primary_column},'
            query_part3 += f' T1.{primary_column} = T2.col{stage_position} and'

        query += (query_part1[:-1] + f' FROM @{stage_table} t) T2 WHERE ' +query_part3[:-3] + ';')

        print(query)

        snowflake_db.query_exec(query)


    query=f'''COPY INTO {table_name} FROM @{table_name}_stage;'''
    snowflake_db.query_exec(query)

    snowflake_db.connection_close()


def drop_stage_snowswl_table(data):
    database_name = data.get("database_name","")
    warehouse = data.get("warehouse","COMPUTE_WH")
    schema = data.get("schema","PUBLIC")
    table_name = data.get("table_name", None)
    stage_table = data.get("stage_table",f'{table_name}_stage' )
    load_type = data.get("load_type",'Snapshot')

    snowflake_db = snowflake_helper({'database_name' : database_name,'warehouse' : warehouse,'schema': schema})

    query = f'REMOVE @{stage_table};'
    snowflake_db.query_exec(query)

    snowflake_db.connection_close()

def update_snowsql_config(data):
    database_name = data.get("database_name","")
    warehouse = data.get("warehouse","COMPUTE_WH")
    schema = data.get("schema","PUBLIC")
    table_name = data.get("table_name", None)

    snowflake_db = snowflake_helper({'database_name' : database_name,'warehouse' : warehouse,'schema': schema})

    query = f''' UPDATE CONFIG.TABLE_CONFIG
                 SET LAST_EXTRACT_DATE = (SELECT MAX(business_date) FROM PUBLIC.{table_name})
                 WHERE TABLE_NAME = '{table_name}';
    '''
    snowflake_db.query_exec(query)

    snowflake_db.connection_close()






