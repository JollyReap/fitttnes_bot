import scrapy
from ..items import FillDatabaseItem
from scrapy.loader import ItemLoader

class HealthSpider(scrapy.Spider):
    name = 'health'
    # allowed_domains = ["https://health-diet.ru"]
    start_urls = ['https://health-diet.ru/table_calorie/']

    def parse(self, response, **kwargs):
        # all_div_blocks = response.xpath('//div[@class="uk-width-1-1"]')
        # for ad_blocks in all_div_blocks:
        all_links = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mzr-tc-group-item-href", " " ))]/@href').extract()
        #name_links = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mzr-tc-group-item", " " ))]/text()').extract()

        for link in all_links:
            yield response.follow("https://health-diet.ru/base_of_food/food_24507/", callback=self.parse_kategories)

    def parse_kategories(self, response, **kwargs):
        loader = ItemLoader(item=FillDatabaseItem())
        name = response.xpath('//td[1]/a/text()').extract()
        call = response.xpath('//td[2]/text()').extract()
        proteins = response.xpath('//td[2]/text()').extract()
        fats = response.xpath('//td[3]/text()').extract()
        carboh = response.xpath('//td[4]/text()').extract()
        params = {
            'name': name,
            "call": call,
            "proteins": proteins,
            "fats": fats,
            "carboh": carboh
        }
        for key, value in params.items():
            loader.add_value(key, value)
        yield loader.load_item()


