import webbrowser, scrapy, os
from scrapy_splash import SplashRequest

# requires docker to be running

#fetch('http://localhost:8050/render.html?url=
# put infront of terminal url

key_value = 0

class SearchSpider(scrapy.Spider):
    name = 'search'

    def start_requests(self):
        userInput = input("Enter search data: ")
        userInput.replace(" ", "+")
        # webbrowser.open('https://www.amazon.co.uk/s?k=' + userInput)
        # doesn't need to open link in final version, just for testing
        start_urls = 'https://www.amazon.co.uk/s?k=' + userInput
        yield SplashRequest(url=start_urls, callback=self.parse)
        # yield scrapy.Request #when not using splash


    def parse(self, response):
        #key_value = 0
        # so our key value does not reset everytime we scrape a page we make it global
        # has to be declared outside the class or it breaks
        global key_value
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

        next_page = response.css('span.s-pagination-strip a.s-pagination-item::attr(href)').get()
        if next_page is not None:
            #checking to see if another page exists
            next_page = response.urljoin(next_page)
            # creating full url
            yield scrapy.Request(next_page, callback=self.parse)
            # yield response with new url


os.system("scrapy crawl search -O crawl_results.json")


# 'https://www.amazon.com/s?k={keyword}&page={page_num}'


