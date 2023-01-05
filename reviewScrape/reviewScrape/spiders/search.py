import webbrowser, scrapy, os
from scrapy_splash import SplashRequest

# requires docker to be running

#fetch('http://localhost:8050/render.html?url=
# put infront of terminal url

class ReviewSpider(scrapy.Spider):
    name = 'reviewSearch'

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

os.system("scrapy crawl reviewSearch -O test.json")

# build second spider for review page
# then combine
