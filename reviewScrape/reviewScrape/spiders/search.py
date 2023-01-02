import webbrowser, scrapy, os
from scrapy_splash import SplashRequest

userInput = input("Enter search data: ")
userInput.replace(" ", "+")
# replaces user's spaces with + for the url
user_link = 'https://www.amazon.co.uk/s?k=' + userInput
webbrowser.open('https://www.amazon.co.uk/s?k=' + userInput)
# doesn't need to open link in final version, just for testing

web_ref = ['https://www.amazon.co.uk']

# - https://youtu.be/mTOXVRao3eA?list=PLRzwgpycm-Fjvdf7RpmxnPMyJ80RecJjv splash

#fetch('http://localhost:8050/render.html?url=

# a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal
# remember hrefs dont like ::text

class ReviewSpider(scrapy.Spider):
    name = 'review'
    start_urls = user_link

    def parse(self, response):
        x = response.css('div.a-section')
        for x in x:
            yield{
                'name': x.css('span.a-color-state.a-text-bold::text').get(),
            } # not working

os.system("scrapy crawl review -O test.json")
# make a regular web crawler that gets product name, price? and link
# then grab review
# use splash guide


