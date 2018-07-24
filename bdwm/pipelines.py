# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class BdwmPipeline(object):
    def process_item(self, item, spider):
    	conn = pymongo.MongoClient(host='localhost', port=27017)
    	db = conn['bdwm']
    	bdwms = db.bdwms
    	bdwms.insert({"title":item["title"], "reply":item["reply"]})

    	with open("content.txt", "a") as fc:
    		fc.write("title: " + item["title"])
    		fc.write("reply: " + item["reply"] + '\n')