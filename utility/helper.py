from mysql.connector import connect
import json

class database_helper:
    def __init__(self,data = 'scrapylearning'):
        database_name = data
        self.create_connection({"database_name":database_name})

    def create_connection(self, data):
        # refer to understand the connection https://www.red-gate.com/simple-talk/databases/mysql/retrieving-mysql-data-python/
        self.conn = connect(option_files = 'D:/Learning/AmazonBooks_DataPipeline/config/dbconnectors.cnf')
        self.conn.database = data['database_name']
        self.conn.autocommit = True
        self.curr = self.conn.cursor()

    def query_exec(self,query):
        self.curr.execute(query)
        result = self.curr.fetchall()
        return result

    def connection_close(self):
        self.conn.close()

    def __del__(self):
        self.conn.close() 


    
