import scrapy
import requests
import json
from pokemon.items import PokemonCard
from scrapy import Request


def get_card_name_list():
    lookups_url = "https://www.pokemon.com/us/api/pokemon-cards/lookups"
    request = requests.get(lookups_url)
    data = request.text
    cards = json.loads(data)
    card_names = cards["names"]
    # lookups = ["Surfing Pikachu", "Surfing Pikachu VMAX"]
    # return lookups
    return card_names


class CardSpider(scrapy.Spider):
    name = 'card'
    allowed_domains = ['pokemon.com']
    start_urls = [f'https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/?cardName={card_name}'
                  for card_name in get_card_name_list()]

    def parse(self, response):
        for card_url in response.css('#cardResults a::attr(href)'):
            yield response.follow(card_url.get(), self.parse_en_card)

    def parse_en_card(self, response):
        item = PokemonCard()
        item['en_name'] = response.css('h1::text').get()
        item['en_url'] = response.css('link[hreflang*=en]::attr(href)').get()
        item['fr_url'] = response.css('link[hreflang*=fr]::attr(href)').get()
        return Request(item['fr_url'], callback=self.parse_fr_card, meta={'item': item})

    def parse_fr_card(self, response):
        item = response.meta['item']
        item['fr_name'] = response.css('h1::text').get()
        return item
