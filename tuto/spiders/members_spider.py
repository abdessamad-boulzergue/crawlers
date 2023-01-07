import scrapy
import re
import json
from bs4 import BeautifulSoup
class QuotesSprider(scrapy.Spider):

    name = "members"
    page_url_pattern = "https://www.fcsi.org/find-a-member-app/data/members.php?page={page}"
    max = 1
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
        
        data = json.loads(response.text)
        yield data
        self.index = self.index +1
        if(self.index<self.max):
            yield scrapy.Request(self.page_url_pattern.format(page=self.index), callback=self.parse)
