import scrapy
import sys
sys.path.append("D:/Learning/AmazonBooks_DataPipeline/utility")
from helper import database_helper
from ..items import AmazonbookSpiderItem_bookreview


class BookreviewSpider(scrapy.Spider):
    name = "bookreview"
    allowed_domains = ["amazon.in"]
    start_urls = ["https://amazon.in"]
    current_bookid = -1

    def start_requests(self):    # function name should not change
        # Get all the serials
        # Melwin refer this https://www.red-gate.com/simple-talk/databases/mysql/retrieving-mysql-data-python/

        bookid_and_urls = self.get_urls()

        for item in bookid_and_urls:
            BookreviewSpider.current_bookid = item[0]
            yield scrapy.Request(url=f'https://amazon.in{item[1]}', callback=self.parse)

    def get_urls(self):
        db = database_helper('amazonebooks')
        query = '''
                    SELECT book_id, book_link from amazone_books 
                    WHERE book_id not in (select book_id from amazonebook_reviews) limit 2;
                '''
        query_output = db.query_exec(query)
        return query_output
        

    def parse(self, response):
        item = AmazonbookSpiderItem_bookreview()

        list_of_reviews = response.xpath('.//div[contains(concat(" ",normalize-space(@class)," ")," a-section ")][contains(concat(" ",normalize-space(@class)," ")," aok-relative ")]')

        for review in list_of_reviews:
            item['book_id'] = BookreviewSpider.current_bookid
            item['reviewer_name'] = review.xpath('.//span[contains(concat(" ",normalize-space(@class)," ")," a-profile-name ")]/text()').extract()
            item['rating'] = review.xpath('.//i[contains(concat(" ",normalize-space(@class)," ")," review-rating ")]/span[contains(concat(" ",normalize-space(@class)," ")," a-icon-alt ")]/text()').extract()
            item['review_title'] = review.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," a-text-bold ")]//span/text()').extract()
            item['review_content'] = review.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," a-expander-partial-collapse-content ")]//span/text()').extract()
            item['reviewed_on'] = review.xpath('.//span[contains(concat(" ",normalize-space(@class)," ")," review-date ")]/text()').extract()
            yield item
        
