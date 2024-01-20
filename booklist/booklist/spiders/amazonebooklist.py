import scrapy
from ..items import BooklistItem


class AmazonebooklistSpider(scrapy.Spider):
    name = "amazonebooklist"
    allowed_domains = ["www.amazon.in"]
    start_urls = ["https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_n_binding_browse-bin%3A1318376031&dc&ds=v1%3AHpaN3DRB2UTHV%2FTZDfOE7kFw6RjBko%2FQD90rLze1hbM&qid=1705754992&rnid=1318374031&ref=sr_nr_p_n_binding_browse-bin_9"]

    def parse(self, response):
        item = BooklistItem
        pass
