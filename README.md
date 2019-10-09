# scrapy-sticky-meta-params

[![Build Status](https://travis-ci.com/heylouiz/scrapy-sticky-meta-params.svg?branch=master)](https://travis-ci.com/heylouiz/scrapy-sticky-meta-params)

A Scrapy spider middleware that forwards meta params through subsequent requests.

## What does it do?

This middleware simplify the process of carrying information through requests and responses on spiders.

## Without the middleware

    class SampleSpider(Spider):
        name = 'without_middleware'
        start_urls = ['https://www.example.com']

        def parse(self, response):
            for param in random(5):
                yield Request('https://www.example.com/next', meta={'param': param}, meta=self.parse_2)

        def parse_2(self, response):
            # Get important information from response
            info = response.xpath('//info/text()').get()
            # We need to get the param from meta and forward it again in this request
            param = response.meta['param']
            yield Request('https://www.example.com/next', meta={'info': info, 'param': param}, meta=self.parse_3)

        def parse_3(self, response):
            # Yield item
            yield {
                'param': response.meta['param'],
                'info': response.meta['info']
            }

## With the middleware

    class SampleSpider(Spider):
        name = 'with_middleware'
        start_urls = ['https://www.example.com']
        sticky_meta_keys = ['param']

        def parse(self, response):
            for param in random(5):
                yield Request('https://www.example.com/next', meta={'param': param}, meta=self.parse_2)

        def parse_2(self, response):
            # Get important information from response
            info = response.xpath('//info/text()').get()
            # We don't need to get the "param" value from meta and resend it.
            yield Request('https://www.example.com/next', meta={'info': info}, meta=self.parse_3)

        def parse_3(self, response):
            # Yield item
            yield {
                'param': response.meta['param'],
                'info': response.meta['info']
            }


## Awesome, how to use it?

To enable the middleware you need to add it to your projects's `SPIDER_MIDDLEWARES` setting in `settings.py`.

    SPIDER_MIDDLEWARES = {
        'scrapy_sticky_meta_params.StickyToMetaSpiderMiddleware': 550,
    }

This middleware needs to be enabled per spider, to this this you need to add the following attribute on your spider:

    sticky_meta_keys = []

You need to fill this list with every Meta key that you want to be forwarded to subsequent requests.
