# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json

class Membertem(scrapy.Item):
    # define the fields for your item here like:
    csv_format = "\n {} , {} , {} , {} ,{}"
    country = scrapy.Field()
    name = scrapy.Field()
    adv_serv = scrapy.Field()
    food_design = scrapy.Field()
    divs=scrapy.Field()
    
    def __str__(self) -> str:
        return self['country']
    
    def toCSVFormat(self):
        return self.csv_format.format(self['country'],self['name'],self['adv_serv'],self['food_design'],self['divs'])