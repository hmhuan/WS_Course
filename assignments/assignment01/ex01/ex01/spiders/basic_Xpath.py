# -*- coding: utf-8 -*-
import scrapy


class BasicXpathSpider(scrapy.Spider):
    name = 'basic_Xpath'
    allowed_domains = ['scrapingclub.com/exercise/detail_basic/']
    start_urls = ['http://scrapingclub.com/exercise/detail_basic/']

    def parse(self, response):
        title = response.xpath("//div[@class='card-body']/h3[@class='card-title']/text()").extract()
        print(title)
