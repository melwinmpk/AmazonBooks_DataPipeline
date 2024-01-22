# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sys
sys.path.append("D:/Learning/AmazonBooks_DataPipeline/utility")
from helper import database_helper
from datetime import datetime


class AmazonbookSpider_booklistPipeline:
    def __init__(self):
        self.db = database_helper('amazonebooks')
        
    def process_item(self, item, spider):
        if spider.current_spider != 'booklist':
            return item
        
        sql_query = f'''
                     INSERT INTO  amazone_books
                     (book_title
                      ,book_amount
                      ,book_author
                      ,book_rating
                      ,book_link) 
                     VALUES (
                     "{item["book_title"][0]}",
                     "{item["book_amount"][0]}",
                     "{(((''.join(item["book_author"])).split("by")[1]).split('|')[0]).strip()}",
                     "{((item["book_rating"][0]).split('out')[0]).strip()}",
                     "{item["book_link"]}"
                     )
        '''
        self.db.query_exec(sql_query)
        return item
    
class AmazonbookSpider_bookreviewPipeline:
    def __init__(self):
        self.db = database_helper('amazonebooks')
        
    def process_item(self, item, spider):
        if spider.current_spider != 'bookreview':
            return item
        
        sql_query = f'''
                     INSERT INTO  amazonebook_reviews
                     (book_id
                    ,reviewer_name
                    ,rating
                    ,review_title
                    ,review_content
                    ,reviewed_on) 
                     VALUES (
                     "{item['book_id']}",
                     "{item['reviewer_name']}",
                     "{(item['rating'].split('out')[0]).strip()}",
                     "{item['review_title']}",
                     "{item['review_content']}",
                     "{datetime.strptime((item['reviewed_on'].split('on')[1]).strip(), '%d %B %Y' )}"
                     )
        '''
        self.db.query_exec(sql_query)
        return item
