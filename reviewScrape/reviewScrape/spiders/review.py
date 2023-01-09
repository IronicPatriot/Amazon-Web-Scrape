import webbrowser, scrapy, os
from scrapy_splash import SplashRequest

class ReviewSpider(scrapy.Spider):
    name = 'review'

    def start_requests(self):
        start_urls = 'https://www.amazon.co.uk/God-of-War-Ragnar%C3%B6k-PS5/dp/B0B6FGSKCQ/ref=sr_1_1?keywords=god+of+war+ragnarok+ps5&qid=1673294296&sprefix=god+of+w%2Caps%2C117&sr=8-1'
        yield SplashRequest(url=start_urls, callback=self.parse)

    def parse(self, response):
        pass