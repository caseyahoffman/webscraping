# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UltaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product = scrapy.Field()    # product name
    brand = scrapy.Field()     # brand name
    rating = scrapy.Field()
    product_url = scrapy.Field()     # product's individual URL


    item = UltaItem()

    item['product'] = product
    item['brand'] = brand
    item['rating'] = rating
    item['product_url'] = product_url