import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links = response.css('tbody a[href^="pep-"]')
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('title::text').get().split(' – ')
        data = {
            'number': title[0].replace('PEP ', ''),
            'name': title[1].replace(' | peps.python.org', ''),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
