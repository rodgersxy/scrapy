import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ReiItem
from scrapy.loader import ItemLoader


class ProductsSpider(CrawlSpider):
    name = "products"
    allowed_domains = ["rei.com"]
    start_urls = ["https://www.rei.com/search?q=camping+deals&ir=q%3Acamping+deals&r=category%3Acamping-and-hiking"]
    
    rules = (
        Rule(LinkExtractor(allow=(r"page=",))),
        Rule(LinkExtractor(allow=(r"product",)), callback="parse_item"),
    )

    def parse_item(self, response):

        I = ItemLoader(item=ReiItem(), response=response)
        I.add_css("title", "h1#product-page-title")
        I.add_css("price", "span#buy-box-product-price")
        I.add_css("item_no", "span#product-item-number")
        I.add_css("rating", "span.cdr-rating__number_15-0-0")
        return I.load_item()
       
