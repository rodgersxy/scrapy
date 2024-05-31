import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

class GfgItemloadersItem(scrapy.Item):
    title = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())