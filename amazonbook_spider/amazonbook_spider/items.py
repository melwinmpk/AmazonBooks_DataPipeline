# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonbookSpiderItem_booklist(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_title = scrapy.Field()
    book_amount = scrapy.Field()
    book_author = scrapy.Field()
    book_rating = scrapy.Field()
    book_link = scrapy.Field()

class AmazonbookSpiderItem_bookreview(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_id = scrapy.Field()
    reviewer_name = scrapy.Field()
    rating = scrapy.Field()
    review_title = scrapy.Field()
    review_content = scrapy.Field()
    reviewed_on = scrapy.Field()
