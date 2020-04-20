import json
import scrapy


class JohnnySeedsSeedsDetailedSeeds(scrapy.Spider):
    name = "detailed_seeds_spider"

    start_urls = []

    with open('json-output/basic-seeds.json') as json_file:
        BASE_URL = 'https://www.johnnyseeds.com/'
        data = json.load(json_file)
        for item in data:
            link = BASE_URL + item['link']
            start_urls.append(link)

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'json-output/detailed-seeds.json'
    }

    def parse(self, response):
        # TODO Implement this scraper
        NAME_SELECTOR = '.product-name ::text'
        SECONDARY_NAME_SELECTOR = '.c-product-header__subheading ::text'
        DESCRIPTION_SELECTOR = '.c-tile__description ::text'
        IMAGE_SELECTOR = 'img.c-image-gallery__main-image ::attr(src)'
        LINK_SELECTOR = 'a.thumb-link ::attr(href)'

        # item = response.meta['item']
        # item['results'] = []
        for seed in response.css(SEED_SELECTOR):
            yield {
                'name': seed.css(NAME_SELECTOR).get().replace('\n', ''),
                'secondary_name': seed.css(SECONDARY_NAME_SELECTOR).get().replace('\n', ''),
                'description': seed.css(DESCRIPTION_SELECTOR).get(),
                'image': seed.css(IMAGE_SELECTOR).get(),
                'link': seed.css(LINK_SELECTOR).get(),
            }
