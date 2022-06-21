# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose


class SensacineTutorialItem(scrapy.Item):
    name = scrapy.Field()
    time_genre = scrapy.Field()
    director = scrapy.Field()
    main_actor = scrapy.Field()
    sec_actor = scrapy.Field()
    puntuaciones = scrapy.Field()
    rating = scrapy.Field()

