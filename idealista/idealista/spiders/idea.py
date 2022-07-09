import scrapy
from ..items import IdealistaItem

class IdeaSpider(scrapy.Spider):
    name = 'idea'
    #allowed_domains = ['idealista.com']
    start_urls = ['https://www.idealista.com/alquiler-viviendas/madrid-provincia/']
    page_number = 2

    def parse(self, response):
        items = IdealistaItem()
        name = response.css('a.item-link::text').extract()
        price = response.css('span.item-price.h2-simulated::text').extract()
        hab = response.css('span.item-detail:nth-child(1)::text').extract()
        mtts = response.css('span.item-detail:nth-child(2)::text').extract()
        floor = response.css('span.item-detail:nth-child(3)::text').extract()
        link = response.css('a.item-link::attr(href)').extract()
        description = response.css('.ellipsis::text').extract()

        items['name'] = name
        items['price'] = price
        items['hab'] = hab
        items['mtts'] = mtts
        items['floor'] = floor
        items['link'] = link
        items['description'] = description

        yield items

        next_page = 'https://www.idealista.com/alquiler-viviendas/madrid/moncloa/pagina-' + str(IdeaSpider.page_number) + '.htm'
        if IdeaSpider.page_number < 40 :
            IdeaSpider.page_number +=1
            yield response.follow(next_page, callback=self.parse)