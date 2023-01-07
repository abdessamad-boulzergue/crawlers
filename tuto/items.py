# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json

class TutoItem(scrapy.Item):
    # define the fields for your item here like:
    quote = scrapy.Field()
    
    def __str__(self) -> str:
        return self['quote']