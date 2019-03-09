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
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)