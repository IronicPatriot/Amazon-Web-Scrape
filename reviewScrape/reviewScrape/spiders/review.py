import scrapy, os, json, webbrowser
from scrapy_splash import SplashRequest

class ReviewSpider(scrapy.Spider):
    name = 'review'

    def start_requests(self):
        # product_link = 'https://www.amazon.co.uk/gp/product/1401263321/ref=ewc_pr_img_1?smid=A3P5ROKL5A1OLE&psc=1'
        # product_link = 'https://www.amazon.co.uk/God-of-War-Ragnar%C3%B6k-PS5/dp/B0B6FGSKCQ/ref=sr_1_1?keywords=god+of+war+ragnarok+ps5&qid=1673294296&sprefix=god+of+w%2Caps%2C117&sr=8-1'

        f = open('crawl_results.json')
        data = json.load(f)
        data_len = len(data)
        # not range
        print(data)

        while True:
            try:
                url_selection = int(input("Which product number would you like to scrape reviews for? "))
                print(url_selection)

                if url_selection > data_len:
                    raise ValueError
                break

            except ValueError:
                print('Please only enter a product number show in the product range.')

        url_selection = url_selection - 1
        product_link = data[url_selection]["LINK"]
        # number/url_selection is which json dictionary to look at, link is our keyword and is CASE SENSITIVE

        # webbrowser.open('https://www.amazon.co.uk' + product_link)
        # open link just for testing

        product_link = 'https://www.amazon.co.uk' + product_link
        # print(product_link)

        f.close()

        yield SplashRequest(url=product_link, callback=self.parse)

    def parse(self, response): # #cm-cr-dp-review-list
        product_review = response.css('div[data-hook=review]')
        for item in product_review:
            yield{
                'USERNAME': item.css('div:nth-child(1)>a>div.a-profile-content>span::text').get(),
                "rating": item.css("*[data-hook*=review-star-rating] ::text").re(r"(\d+\.*\d*) out"),
                # from example code, remove zero to get all
                # 'TEXT': item.css("span[data-hook=review-body] ::text").getall(),
                'TEXT': "".join(item.css("span[data-hook=review-body] ::text").getall()).strip().removesuffix('Read more'),
                # has to be a getall or just gets the first line of review
                # join is Python code not scrapy, takes all separate strings and merges them together
            }

os.system("scrapy crawl review -O product-reviews.json")

