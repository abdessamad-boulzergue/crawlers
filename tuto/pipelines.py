# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from scrapy.exceptions import NotConfigured
from tuto.items import Membertem

class TutoPipeline:

    csv_header = "country , Email , Food Facility Design , Management Advisory Services , MTC"
    csv_data_f = "\n {} , {} , {} , {} ,{}"
    def process_item(self, item, spider):       
       
          # calling dumps to create json data.
        for it in item:
            self.fileCsv.write(it.toCSVFormat())
        return item
 
    def open_spider(self, spider):
        self.file = open('result.json', 'w')
        self.fileCsv = open('result.csv', 'w')
        self.fileCsv.write(self.csv_header)
 
    def close_spider(self, spider):
        self.file.close()
        self.fileCsv.close()
class FilterPipeline:

    def process_item(self, item, spider):         
          # calling dumps to create json data.
        items = []
        for v in item.values():
            if v["Details"]["Country"] =="United States":
                
                det = v["Details"]
                adv_serv ="Yes" if len(v['MAS'])>0 else "No"
                food_design="Yes" if len(v["FFD"])>0 else "No"
                divs= " ".join([getDivs(id) for id in v['Divs']])
                name = (det['Lname'] + det['Fname']).replace(',',' ')

                items.append(Membertem(
                    name = name,
                    country = v["Details"]["Country"],
                    adv_serv = adv_serv,
                    food_design = food_design,
                    divs=divs
                ))
            
        return items


def getDivs(id):
    divs= {
        '24':"Americas",
        '25':"APD",
        '26':'EAME'
    }
    return divs[id]