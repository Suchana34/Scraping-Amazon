# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapamazonItem

class AmazonbooksSpider(scrapy.Spider):
    name = 'amazonbooks'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?k=best+seller+books&crid=3U6CNVJEO5BSS&sprefix=best+selling%2Caps%2C-1&ref=nb_sb_noss_2']

    def parse(self, response):
        item = ScrapamazonItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image-fixed-height .s-image').css('::attr(src)').extract()

        item['product_name'] = product_name
        item['product_author'] = product_author
        item['product_price'] = product_price
        item['product_imagelink'] = product_imagelink

        yield item
        
