# -*- coding: utf-8 -*-
import scrapy
import json


class DirectorsSpider(scrapy.Spider):
    name = 'directors'
    allowed_domains = ['imdb.com']
    start_urls = []
    with open ('C:\Users\Hovo\Desktop\HOVO\AUA\Data_scraping\Homeworks\Homework_5\imbd\movies.json') as f: 
       	x=f.read()
    	link=json.loads(x)
    	for i in range(10):
    		start_urls.append(link[i]['URL'])

    def parse(self, response):
        yield{
        "movie": response.xpath('//*[contains(@class, "title_wrapper")]/h1/text()').extract_first(),
        "director": response.xpath('//*[contains(@class, "credit_summary_item")]/span/a/span/text()').extract_first()
        }