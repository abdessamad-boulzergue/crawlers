# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from scrapy.exceptions import NotConfigured
from tuto.items import TutoItem

class TutoPipeline:

    
    def process_item(self, item, spider):       
       
          # calling dumps to create json data.
        line = json.dumps(item) + "\n"  
        self.file.write(line)
        return item
 
    def open_spider(self, spider):
        self.file = open('result.json', 'w')
 
    def close_spider(self, spider):
        self.file.close()

class MapPipeline:

    def process_item(self, item, spider):       
       
        return TutoItem(quote=item['name'])