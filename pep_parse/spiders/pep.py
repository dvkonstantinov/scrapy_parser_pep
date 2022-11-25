import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.xpath(
            '//table[contains(@class, "pep-zero-table")]/tbody/tr/td['
            '2]/a/@href').getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        h1 = response.xpath('//h1[@class="page-title"]/text()').get()
        number = h1.split(' – ')[0].split(' ')[1]
        name = h1.split(' – ')[1]
        status = response.xpath(
            '//dl[contains(@class, "rfc2822")]/dt[contains(., '
            '"Status")]/following-sibling::dd[1]/text()').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
