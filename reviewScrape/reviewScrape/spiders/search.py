import webbrowser, scrapy, os
from scrapy_splash import SplashRequest

# requires docker to be running

#fetch('http://localhost:8050/render.html?url=
# put infront of terminal url

class SearchSpider(scrapy.Spider):
    name = 'search'

    def start_requests(self):
        userInput = input("Enter search data: ")
        userInput.replace(" ", "+")
        webbrowser.open('https://www.amazon.co.uk/s?k=' + userInput)
        # doesn't need to open link in final version, just for testing
        start_urls = 'https://www.amazon.co.uk/s?k=' + userInput
        # start_urls = 'https://www.amazon.co.uk/s?k=god+of+war+ragnarok+ps5&sprefix=go%2Caps%2C119&ref=nb_sb_ss_ts-doa-p_1_2'
        yield SplashRequest(url=start_urls, callback=self.parse)
        # yield scrapy.Request (when not using splash)

    def parse(self, response):
        product = response.css('div.s-result-item[data-component-type=s-search-result]')
        for item in product:
                yield{
                    'NAME': item.css('h2>a>span::text').get(),
                    'PRICE': item.css('.a-offscreen::text').get(default = 'No Price Available'),
                    'LINK': item.css('h2>a').attrib['href'],
                    # remember hrefs dont like ::text
                }

os.system("scrapy crawl search -O test.json")

# build second spider for review page
# then combine

# #customer_review-R33A3MQMORZ8OW

#customer_review-R33A3MQMORZ8OW>div.a-row.a-spacing-small.review-data

# https://www.amazon.co.uk/God-of-War-Ragnar%C3%B6k-PS5/dp/B0B6FGSKCQ/ref=sr_1_1?keywords=god%2Bof%2Bwar%2Bragnarok%2Bps5&qid=1673294296&sprefix=god%2Bof%2Bw%2Caps%2C117&sr=8-1&th=1

# response.css("span[data-hook=review-body] ::text").getall()

# get just gives a bunch of "nnnnn", getall gets all reviews plus that garbage, so partly working