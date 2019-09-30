import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_url = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            yield {
                'title': title,
                'author': author,
                'tag': tag
            }