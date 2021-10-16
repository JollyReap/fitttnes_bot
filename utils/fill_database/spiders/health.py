import scrapy
from ..loaders import HealthLoader


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
        tbody = response.xpath('//tbody/tr').extract()
        # for body in tbody:
        #     link = body.xpath('/td[0]/a/@href/text()').extract()
        #     yield {
        #         's': link
        #     }
        yield {
            's': tbody
        }
