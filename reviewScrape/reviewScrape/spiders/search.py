import webbrowser, scrapy, os
from scrapy_splash import SplashRequest

'''userInput = input("Enter search data: ")
userInput.replace(" ", "+")
# replaces user's spaces with + for the url
user_link = 'https://www.amazon.co.uk/s?k=' + userInput
webbrowser.open('https://www.amazon.co.uk/s?k=' + userInput)
# doesn't need to open link in final version, just for testing

web_ref = ['https://www.amazon.co.uk']'''

# - https://youtu.be/mTOXVRao3eA?list=PLRzwgpycm-Fjvdf7RpmxnPMyJ80RecJjv splash

#fetch('http://localhost:8050/render.html?url=

# a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal
# remember hrefs dont like ::text

class ReviewSpider(scrapy.Spider):
    name = 'review'

    def start_requests(self):
        start_urls = 'https://www.amazon.co.uk/s?k=god+of+war+ragnarok+ps5&sprefix=go%2Caps%2C119&ref=nb_sb_ss_ts-doa-p_1_2'
        yield SplashRequest(url=start_urls, callback=self.parse)
        # yield scrapy.Request when not using splash

    def parse(self, response):
        product = response.css('div.s-result-item[data-component-type=s-search-result]')
        for item in product:
            yield {
                'name': item.css('h2>a>span::text').get(),
                # link
            }

os.system("scrapy crawl review -O test.json")

#use amazon vid as guide, but learn how to get right html elements on your own
