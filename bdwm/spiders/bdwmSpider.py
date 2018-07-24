# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import BdwmItem

class BdwmspiderSpider(scrapy.Spider):
    name = 'bdwmSpider'
    allowed_domains = ['bbs.pku.edu.cn']
    start_urls = ['https://bbs.pku.edu.cn/v2/thread.php?bid=690&mode=topic']
    bdurl = 'https://bbs.pku.edu.cn/v2/thread.php?bid=690&mode=topic&page='
    for i in range(1, 255):
    	bdwmurl = bdurl + str(i)
    	start_urls.append(bdwmurl)

    def parse(self, response):
    	# 实例一个容器，保存得到的数据
    	request = "https://bbs.pku.edu.cn/v2/"
    	item = BdwmItem()
    	urls = response.xpath('//div[@id="page-content"]/div[@id="page-thread"]/div[@id="board-body"]/div[@id="list-body"]/div[@id="list-content"]/div/a/@href').extract()
    	
    	# 爬取部分，使用xpath获取想要的数据
    	for doc in urls:
    		xqurl = request + doc
    		yield scrapy.Request(xqurl, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
    	item = BdwmItem()
    	title  = response.xpath('//div[@id="post-read"]/header/h3/text()')[0].extract()
    	reply = response.xpath('//p[@title="心理咨询师"]/ancestor::div[@class="post-owner"]/following-sibling::div[@class="post-main"]/div[@class="content"]/div[@class="body file-read image-click-view"]/p/text()').extract()
    	if reply == []:
    		item["title"] = str(title) + '\n'
    		item["reply"] = "无心理咨询师回复！\n"
    	else:
    		item["title"] = str(title) + '\n'
    		item["reply"] = str(reply[0]) + '\n'
    	yield item






