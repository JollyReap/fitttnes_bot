import scrapy
from ..loaders import HealthLoader


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
        loader = HealthLoader(response=response)
        product = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "uk-table-condensed", " " ))]//a/text()').extract()
        calories = response.xpath('//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]/text()').extract()
        proteins = response.xpath('//td[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]/text()').extract()
        fats = response.xpath('//td[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]/text()').extract()
        carbohydrates = response.xpath('//td[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]/text()').extract()
        name_link = response.xpath('//h1/text()').extract()
        for name_links in name_link:
            name_links = name_links.split(' ')
            name__link = name_links[::2]
        info = {
            "product": product,
            "calories": calories,
            "proteins": proteins,
            "fats": fats,
            "carbohydrates": carbohydrates,
            "link":  response.text,
            "name_link": name__link
        }
        for key, value in info.items():
            loader.add_value(key, value)

        info = loader.load_item()