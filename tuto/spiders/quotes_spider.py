import scrapy
import re
import json
from bs4 import BeautifulSoup
class QuotesSprider(scrapy.Spider):

    name = "quotes"
    allowed_domains=["horecava.nl"]
    page_url_pattern = "https://www.horecava.nl/leveranciers/page/{page}/"
    max = 0
    index = 1
    start_urls = [
        page_url_pattern.format(page=1)
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def getContacts(self , contacts):
        pass

    def parse_article(self, response):
        if len(response.css('div.supplier-article-top-section h1').getall())>0:
            contacts = response.css('p.contact-container::text').getall();
            yield {
                'name': response.css("div.supplier-article-top-section h1::text").get(),
                'email':re.findall("\w+@\w+.\w+",str(contacts)),
                'phone':re.findall("\+[0-9\-\(\)]*",str(contacts))
            }

    def parse(self, response):
        
        for quote in response.css('div.articleblock__content'):
            next_page = quote.css('.articleblock__content__infobar a::attr(href)')[1].get()
            if next_page is not None:
                #next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse_article)

        self.index = self.index +1
        if(self.index<self.max):
            yield scrapy.Request(self.page_url_pattern.format(page=self.index), callback=self.parse)
