# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, Join, MapCompose
from w3lib.html import remove_tags


def clean_data(value):
    chars_to_remove = ["$", "Item", "#"]
    for char in chars_to_remove:
        if char in value:
            value = value.replace(char, "")

    return value.strip()

class ReiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=TakeFirst(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=TakeFirst(),
    )
    item_no = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=TakeFirst(),
    )
    rating = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=TakeFirst(),
    )
