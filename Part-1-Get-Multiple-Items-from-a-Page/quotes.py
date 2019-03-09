# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
        	text = quote.css('span.text::text').extract_first()
        	author = quote.css('small.author::text').extract_first()
        	tags = quote.css('a.tag::text').extract()

        	item = {
        		'text': text,
        		'author': author,
        		'tags': tags
        	}

        	yield(item)
