from scrapy import Spider, Request
from ulta.items import UltaItem

class UltaSpider(Spider):
    name = 'ulta_spider'
    allowed_urls = ['https://www.ulta.com']
    start_urls = ['https://www.ulta.com/skin-care-face-moisturizer?N=27h9']

    def parse(self, response):
        # find all the products on the page
        rows = response.xpath('//ul[@id="foo16"]/li/div[@class="productQvContainer"]')

        for row in rows:

            product = row.xpath('.//p[@class="prod-desc"]/a/text()').extract_first().strip()
            brand = row.xpath('.//h4[@class="prod-title"]/a/text()').extract_first().strip()
            rating = row.xpath('./a/label/text()').extract_first()
            product_url = row.xpath('./a/@href').extract_first()

        # initialize UltaItem instance for each movie
        item = UltaItem()
        item['product'] = product
        item['brand'] = brand
        item['rating'] = rating
        item['product_url'] = product_url

        yield item