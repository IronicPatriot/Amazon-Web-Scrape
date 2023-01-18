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
        # yield scrapy.Request #when not using splash

    def parse(self, response):
        key_value = 0
        user_url = response.css('div.s-result-item[data-component-type=s-search-result]')
        for product in user_url:
                key_value += 1
                yield{
                    'PRODUCT_NUMBER': key_value,
                    'PRODUCT_NAME': product.css('h2>a>span::text').get(),
                    'PRICE': product.css('.a-offscreen::text').get(default = 'No Price Available'),
                    'LINK': product.css('h2>a').attrib['href'],
                    # remember hrefs dont like ::text
                }

os.system("scrapy crawl search -O crawl_results.json")

