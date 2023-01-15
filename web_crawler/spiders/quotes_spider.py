import scrapy
import re
import json
from bs4 import BeautifulSoup
class QuotesSprider(scrapy.Spider):

    name = "creditcards"
    start_urls = [
        "https://www.creditcards.com/reviews/cash-back/?orderby=product.name&order=ASC"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse_article(self, response):
        
        review_head = response.css('div.review-head').get()
        name = response.css('h1.review-header::text').get()
        entry_content = response.css('div.entry-content').get()
        review_feature = []
        for cell in response.css('td.overview-category-cell'):
            title = cell.css("p>strong::text").get()
            reviews = cell.css("p::text").get()
            reviews  = reviews if reviews is not None else " - ".join(cell.css("li::text").getall()) 
            feature = {
                "title":title,
                "reviews" : reviews
            }
            review_feature.append(feature)

        
        yield{
            "name" : name,
            "overview_category_title" : review_feature
        }


    def parse(self, response):
        
        for card in response.css('div.card-box'):
            next_page = card.css('p.read-full-review a::attr(href)').get()
            if next_page is not None:
                #next_page = response.urljoin(next_page)
                yield response.follow(next_page, callback=self.parse_article)