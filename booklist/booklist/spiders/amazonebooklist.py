from pathlib import Path
import scrapy
from ..items import BooklistItem


class AmazonebooklistSpider(scrapy.Spider):
    name = "amazonebooklist"
    allowed_domains = ["www.amazon.in"]
    start_urls =  ["https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_n_binding_browse-bin%3A1318376031&dc&qid=1705764773&rnid=1318374031&ref=sr_nr_p_n_binding_browse-bin_9&ds=v1%3ADnZrpwSN6HQUdKmMPrF0hUMVrGOY%2FbMRz0yDiGbpnnw"]
    
    def parse(self, response):
        item_container = BooklistItem()

        item_list = response.xpath('.//div[contains(concat(" ",normalize-space(@class)," ")," puis-card-border ")]/div[contains(concat(" ",normalize-space(@class)," ")," a-section ")]/div[contains(concat(" ",normalize-space(@class)," ")," puisg-row ")]')
        
        for items in item_list:
            item_container["book_title"] = items.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," a-color-base ")][contains(concat(" ",normalize-space(@class)," ")," a-text-normal ")]/text()').extract()
            item_container["book_amount"] = items.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," a-price-whole ")]/text()').extract()
            item_container["book_author"] = items.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," a-color-secondary ")]//*[contains(concat(" ",normalize-space(@class)," ")," a-row ")]//*[contains(concat(" ",normalize-space(@class)," ")," a-size-base ")]/text()').extract()
            item_container["book_rating"] = items.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," aok-align-bottom ")]//*[contains(concat(" ",normalize-space(@class)," ")," a-icon-alt ")]/text()').extract()
            item_container["book_link"] = items.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," a-link-normal ")][contains(concat(" ",normalize-space(@class)," ")," a-text-normal ")]/@href')[0].extract()
            

            yield item_container


        # Use of CSS insted of Xpath
        '''
        item_list = response.css('.puis-card-border > .a-section > .puisg-row')
        

        for items in item_list:
            item_container["book_title"] = items.css('.a-color-base.a-text-normal::text').extract()
            item_container["book_amount"] = items.css('.a-price-whole::text').extract()
            item_container["book_author"] = items.css('.a-color-secondary .a-row .a-size-base::text').extract()
            item_container["book_rating"] = items.css('.aok-align-bottom .a-icon-alt::text').extract()
            item_container["book_link"] = items.css('.a-link-normal.a-text-normal::attr(href)').extract()

            yield item_container
        '''