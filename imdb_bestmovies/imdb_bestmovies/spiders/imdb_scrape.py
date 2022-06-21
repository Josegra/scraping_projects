import scrapy
from ..items import ImdbBestmoviesItem

class ImdbScrapeSpider(scrapy.Spider):
    name = 'imdb_scrape'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']
    page_number = 51

    def parse(self, response):
        items = ImdbBestmoviesItem()
        title = response.css('.lister-item-header a::text').extract()
        year = response.css('.text-muted.unbold::text').extract()
        run_time = response.css('.runtime::text').extract()
        genre = response.css('.genre::text').extract()
        imdb_score = response.css('.ratings-imdb-rating strong::text').extract()
        metascore_score = response.css('.favorable::text').extract()
        summary = response.css('.ratings-bar+ .text-muted::text').extract()
        director = response.css('.text-muted+ p a:nth-child(1)::text').extract()
        lead_actor = response.css('.lister-item-content .ghost+ a::text').extract()
        supporting_actor = response.css('a:nth-child(4)::text').extract()
        tritagonist_Actor = response.css('a:nth-child(5)::text').extract()
        votes = response.css('.sort-num_votes-visible span:nth-child(2)::text').extract()
        box_office = response.css('.sort-num_votes-visible span:nth-child(5)::text').extract()
        top250_position = response.css('.top-chart-rank+ span::text').extract()

        items['title'] = title
        items['year'] = year
        items['run_time'] = run_time
        items['genre'] = genre
        items['imdb_score'] = imdb_score
        items['metascore_score'] = metascore_score
        items['summary'] = summary
        items['director'] = director
        items['lead_actor'] = lead_actor
        items['supporting_actor'] = supporting_actor
        items['tritagonist_Actor'] = tritagonist_Actor
        items['votes'] = votes
        items['box_office'] = box_office
        items['top250_position'] = top250_position

        yield items

        next_page = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=' + str(ImdbScrapeSpider.page_number) + '&ref_=adv_nxt'
        if ImdbScrapeSpider.page_number < 251:
            ImdbScrapeSpider.page_number += 50
            yield response.follow(next_page, callback=self.parse)





