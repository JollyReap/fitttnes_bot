# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
# from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, Join, Identity, TakeFirst


def add_n(text: str) -> str:
    try:
        text = text.replace('",', '\n')
    except ValueError as err:
        print(err)
    return text


def change_text(text: str) -> str:
    try:
        text = text.replace(' ', '').replace('\n', '-')
    except ValueError as err:
        print(err)
    return text


class FillDatabaseItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(
        input_processor=Join(),
        output_processor=MapCompose(add_n),
    )
    call = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity(),
    )
    proteins = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity(),
    )
    fats = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity(),
    )
    carboh = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity(),
    )

