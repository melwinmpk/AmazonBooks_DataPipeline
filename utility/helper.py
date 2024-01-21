import mysql.connector
import json

class database_helper:
    def __init__(self,data = 'scrapylearning'):
        database_name = data

        f = open('D:/Learning/AmazonBooks_DataPipeline/utility/databasecredentials.json')
        data = json.load(f)
        f.close()

        self.create_connection({
            "database_name":database_name,
            "user":data.get("user","root"),
            "password":data.get("password","welcome123"),
            "host":data.get("host","127.0.0.1")
        })

    def create_connection(self, data):
        self.conn = mysql.connector.connect(
                        database=data["database_name"]
                        ,user=data["user"]
                        ,password=data["password"]
                        ,host=data["host"]
        )
        self.conn.autocommit = True
        self.curr = self.conn.cursor()

    def query_exec(self,query):
        self.curr.execute(query)
        self.conn.commit()

    def connection_close(self):
        self.conn.close()

    def __del__(self):
        self.conn.close() 


    
