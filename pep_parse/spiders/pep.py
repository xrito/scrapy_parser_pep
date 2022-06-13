import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.xpath('//section[@id="numerical-index"]')
        tbody = all_peps.css('tbody')
        for tr in tbody.css('tr'):
            pep_link = tr.css('a').attrib['href']
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': (
                response.css('li:contains(" » ") + li + li::text').get()
            ),
            'name': response.css('h1.page-title::text').get(),
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
