# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TableScrapSpider:
    name = scrapy.Field()
    Domain = scrapy.Field()
    Priority = scrapy.Field()
    # Priority = scrapy.Field()
class WebscrapItem(scrapy.Item):
    # define the fields for your item here lik
    pass
