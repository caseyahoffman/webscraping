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
    avg_review = scrapy.Field()
    n_review = scrapy.Field() # number of reviews
    price = scrapy.Field()
    product_url = scrapy.Field()     # product's individual URL
