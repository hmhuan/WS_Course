# -*- coding: utf-8 -*-
import scrapy


class ex01(scrapy.Spider):
    name = 'ex01'
    allowed_domains = ['scrapingclub.com/exercise/detail_basic/']
    start_urls = ['https://scrapingclub.com/exercise/detail_basic/']

    def parse(self, response):
        title = response.xpath("//h3[@class='card-title']/text()").extract()
        price = response.xpath("//h4/text()").extract()
        print(title)
        print(price)
        # yield {'title': title,
        #         'price': price}
