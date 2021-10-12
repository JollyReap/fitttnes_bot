from itemloaders.processors import MapCompose, TakeFirst, Identity
# from scrapy.loader import ItemLoader
import scrapy


def change_text(text: str) -> str:
    try:
        text = text.replace('\n', "").split(' ')
    except Exception as err:
        print(err)

    return text


def name_link(text: str) -> str:
    try:
        text = text[::1]
    except Exception as err:
        print(err)
    return text


class HealthLoader(scrapy.Item):
    product = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity()
    )
    calories = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity()
    )
    proteins = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity()
    )
    fats = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity()
    )
    carbohydrates = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity()
    )
    link = scrapy.Field(
        input_processor=MapCompose(change_text),
        output_processor=Identity()
    )
    name_link = scrapy.Field(
        input_processor=MapCompose(name_link),
        output_processor=Identity()
    )