import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator

with DAG(
    dag_id="WebScraping_DAG",
    start_date=datetime.datetime(2024,1,1),
    schedule=None
    ) as dag:

    Booklist_task = BashOperator(
            task_id='Booklist_Data_Scrapping',
            bash_command='''cd /home/de/Projects/AmazonBooks_DataPipeline/amazonbook_spider
                            scrapy crawl booklist
            '''
        )
    Bookreview_task = BashOperator(
            task_id='Bookreview_Data_Scrapping',
            bash_command='''cd /home/de/Projects/AmazonBooks_DataPipeline/amazonbook_spider
                            scrapy crawl bookreview
            '''
        )

    Start = EmptyOperator(task_id="Start")
    End   = EmptyOperator(task_id="End")
    Start >> Booklist_task >> Bookreview_task >> End
