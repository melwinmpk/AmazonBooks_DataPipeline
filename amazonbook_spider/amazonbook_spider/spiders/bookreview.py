import scrapy


class BookreviewSpider(scrapy.Spider):
    name = "bookreview"
    allowed_domains = ["amazon.in"]
    start_urls = ["https://amazon.in"]

    def parse(self, response):
        pass
