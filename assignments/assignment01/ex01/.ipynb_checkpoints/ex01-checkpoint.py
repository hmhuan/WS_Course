# -*- coding: utf-8 -*-
import scrapy


class Ex01Spider(scrapy.Spider):
    name = 'ex01'
    allowed_domains = ['https://scrapingclub.com/exercise/detail_basic/']
    start_urls = ['http://https://scrapingclub.com/exercise/detail_basic//']

    def parse(self, response):
        title = response.xpath("//h3[@class='card-title']/text()").extract()
        print(title)
