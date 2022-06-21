import scrapy
from ..items import SensacineTutorialItem


class SensacineTutorialSpider(scrapy.Spider):
    name = 'sensacine_tutorial'
    page_number = 2
    allowed_domains = ['sensacine.com']
    start_urls = ['https://www.sensacine.com/peliculas/mejores-peliculas/?page=1']

    def parse(self, response):
        items = SensacineTutorialItem()
        name = response.css('.meta-title-link::text').extract()
        time_genre = response.css('.meta-body-info::text').extract()
        director = response.css('.blue-link::text').extract()
        main_actor = response.css('.meta-body-actor .light+ a::text').extract()
        sec_actor = response.css('.meta-body-actor a:nth-child(3)::text').extract()
        puntuaciones = response.css('.rating-title::text').extract()
        rating = response.css('.stareval-note::text').extract()

        items['name'] = name
        items['time_genre'] = time_genre
        items['director'] = director
        items['main_actor'] = main_actor
        items['sec_actor'] = sec_actor
        items['puntuaciones'] = puntuaciones
        items['rating'] = rating

        yield items

        next_page = 'https://www.sensacine.com/peliculas/mejores-peliculas/?page='+ str(SensacineTutorialSpider.page_number)
        if SensacineTutorialSpider.page_number < 30:
            SensacineTutorialSpider.page_number += 1
            yield response.follow(next_page,callback=self.parse)


