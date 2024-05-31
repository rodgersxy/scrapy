import scrapy
from scrapy.loader import ItemLoader
from ..items import GfgItemloadersItem

class GfgLoadbookdataSpider(scrapy.Spider):
    name = 'gfg_loadbookdata'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for book in response.xpath('//article[@class="product_pod"]'):
            loader = ItemLoader(item=GfgItemloadersItem(), selector=book)
            loader.add_xpath('title', './/h3/a/@title')
            loader.add_xpath('price', './/p[@class="price_color"]/text()')
            yield loader.load_item()