# -*- coding: utf-8 -*-
import scrapy


class ex02(scrapy.Spider):
    name = 'ex02'
    allowed_domains = ['scrapingclub.com/exercise/detail_json/']
    start_urls = ['https://scrapingclub.com/exercise/detail_json/']

    def parse(self, response):
        print(response.text)
        title = response.xpath("//h3[@class='card-title']/text()").extract()
        price = response.xpath("//h4/text()").extract()
    
        print(title)
        print(price)
