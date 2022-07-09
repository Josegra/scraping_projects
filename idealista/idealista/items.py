# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IdealistaItem(scrapy.Item):

    name = scrapy.Field()
    price = scrapy.Field()
    hab = scrapy.Field()
    mtts = scrapy.Field()
    floor = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()

