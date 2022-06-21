# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbBestmoviesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    year = scrapy.Field()
    run_time = scrapy.Field()
    genre = scrapy.Field()
    imdb_score = scrapy.Field()
    metascore_score = scrapy.Field()
    summary = scrapy.Field()
    director = scrapy.Field()
    lead_actor = scrapy.Field()
    supporting_actor = scrapy.Field()
    tritagonist_Actor = scrapy.Field()
    votes = scrapy.Field()
    box_office = scrapy.Field()
    top250_position = scrapy.Field()



