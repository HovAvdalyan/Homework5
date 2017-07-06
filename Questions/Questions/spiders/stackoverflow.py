# -*- coding: utf-8 -*-
import scrapy


class StackoverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = []
    
    i=1
    while i<4:
    	url = "https://stackoverflow.com/questions/tagged/python/?page=" + str(i) +"&sort=newest&pageSize=50"
    	start_urls.append(url)
    	i+=1
    	

    def parse(self, response):
        data=response.css("a.question-hyperlink")
        for j in data:
      		question=j.css("::text").extract_first()
      		url=j.css("::attr(href)").extract_first()
      		yield{
 			     'Question': question,
 			     'URL': url
 			}
