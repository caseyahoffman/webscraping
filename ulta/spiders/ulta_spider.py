from scrapy import Spider, Request
from ulta.items import UltaItem

class UltaSpider(Spider):
    name = 'ulta_spider'
    allowed_urls = ['https://www.ulta.com']
    start_urls = ['https://www.ulta.com/skin-care-face-moisturizer?N=27h9']


    def parse(self, response):

        # 'url_list' will contain a list of all result page URLS
        page1 = 'https://www.ulta.com/skin-care-face-moisturizer?N=27h9'
        page_parts = ['', '&No=96&Nrpp=96', '&No=192&Nrpp=96', '&No=288&Nrpp=96', '&No=384&Nrpp=96', '&No=480&Nrpp=96', '&No=576&Nrpp=96', '&No=672&Nrpp=96']
        url_list = [str(page1 + page) for page in page_parts]

        for url in url_list:

            yield Request(url=url, callback=self.parse_result_page)  
    
    def parse_result_page(self, response):

        rows = response.xpath('//div[@class="productQvContainer"]')
        for row in rows:

            try:
                brand = row.xpath('./div[@class="prod-title-desc"]//a/text()').extract()[0].strip()
                product = row.xpath('./div[@class="prod-title-desc"]//a/text()').extract()[1].strip()
                avg_review = row.xpath('.//label[@class="sr-only"]/text()').extract_first()
                n_review = row.xpath('./span[@class="prodCellReview"]/a/text()').extract_first()
                price = row.xpath('./div/span/text()').extract_first()
                product_url = row.xpath('./a/@href').extract_first()
            except Exception as e:
                print(e)
            

            item = UltaItem()
            item['product'] = product
            item['brand'] = brand
            item['avg_review'] = avg_review
            item['n_review'] = n_review
            item['price'] = price
            item['product_url'] = product_url

            yield item
            
        
    #     for url in url_list:

    #         yield Request(url=url, callback=self.parse_product_page)

    # def parse_product_page(self, response):

    #     pass
