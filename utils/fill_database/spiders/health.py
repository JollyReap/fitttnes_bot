import scrapy
from ..loaders import HealthLoader
from scrapy.loader import ItemLoader

class HealthSpider(scrapy.Spider):
    name = 'health'
    # allowed_domains = ["https://health-diet.ru"]
    start_urls = ['https://health-diet.ru/table_calorie/']

    def parse(self, response, **kwargs):
        # all_div_blocks = response.xpath('//div[@class="uk-width-1-1"]')
        # for ad_blocks in all_div_blocks:
        loader = HealthLoader(response=response)
        all_links = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mzr-tc-group-item-href", " " ))]/@href').extract()
        #name_links = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mzr-tc-group-item", " " ))]/text()').extract()

        for link in all_links:
            yield response.follow("https://health-diet.ru/base_of_food/food_24507/", callback=self.parse_kategories)

    def parse_kategories(self, response, **kwargs):
        loader = ItemLoader(item=HealthLoader(), selector=response.xpath, response=response)
        loader.add_xpath("product", '//*[contains(concat( " ", @class, " " ), concat( " ", "uk-table-condensed", " " ))]//a/text()')
        loader.add_xpath("calories", '//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]/text()')
        loader.add_xpath('proteins','//td[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]/text()')
        loader.add_xpath('fats', '//td[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]/text()')
        loader.add_xpath('carbohydrates','//td[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]/text()')
        loader.add_xpath('name_link','//h1/text()')

        yield loader.load_item()
        # for name_links in name_link:
        #     name_links = name_links.split(' ')
        #     name__link = name_links[::2]
        # info = {
        #     "product": product,
        #     "calories": calories,
        #     "proteins": proteins,
        #     "fats": fats,
        #     "carbohydrates": carbohydrates,
        #     "link":  response.text,
        #     "name_link": name__link
        # }
        # for key, value in info.items():
        #     loader.add_value(key, value)
        #
        # info = loader.load_item()