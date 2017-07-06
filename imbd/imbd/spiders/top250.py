# -*- coding: utf-8 -*-
import scrapy


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/chart/top']

    def parse(self, response):
        table=response.css("tr")[1:-2]
        avg_rating=[]

        for i in table:
        	ranking=i.css("td.titleColumn::text").re("([0-9]+)[.]")
    		title=i.css("td.titleColumn a::text").extract_first()
    		url="http://www.imdb.com"+str(i.css("td.titleColumn a::attr(href)").extract_first())
    		release_year=i.css("span.secondaryInfo::text").extract_first()
    		rating=str(i.css("td.ratingColumn.imdbRating strong::text").extract_first())

    		
    		rating=float(rating)
    		avg_rating.append(rating)
    		
    		yield{	"Ranking":ranking,
    				"Title":title,
    				"URL":url,
    				"Year":release_year,
    				"Rating":rating	
    					}
        
        avg=sum(avg_rating)/len(avg_rating)
    	yield{
    	"Average":avg
    	}
