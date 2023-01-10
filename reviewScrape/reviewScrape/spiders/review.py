import webbrowser, scrapy, os
from scrapy_splash import SplashRequest

class ReviewSpider(scrapy.Spider):
    name = 'review'

    def start_requests(self):
        start_urls = 'https://www.amazon.co.uk/God-of-War-Ragnar%C3%B6k-PS5/dp/B0B6FGSKCQ/ref=sr_1_1?keywords=god+of+war+ragnarok+ps5&qid=1673294296&sprefix=god+of+w%2Caps%2C117&sr=8-1'
        yield SplashRequest(url=start_urls, callback=self.parse)

    def parse(self, response): # #cm-cr-dp-review-list
        review = response.css('div[data-hook=review]')
        for item in review:
            yield{
                'USERNAME': item.css('div:nth-child(1)>a>div.a-profile-content>span::text').get(),
                "rating": item.css("*[data-hook*=review-star-rating] ::text").re(r"(\d+\.*\d*) out"),
                # from example code, remove zero to get all
                'TEXT': item.css("span[data-hook=review-body] ::text").getall(),
                # has to be a getall or just gets the first line of review

            }

os.system("scrapy crawl review -O test-two.json")

# remove junk from text get