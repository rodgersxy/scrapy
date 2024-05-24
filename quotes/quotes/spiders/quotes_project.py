import scrapy
from json import loads as json_loads


class QuotesProjectSpider(scrapy.Spider):
    name = "quotes_project"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        json_response = json_loads(response.body)
        quotes = json_response["quotes"]

        for quote in quotes:
            yield {
                'author': quote.get('author').get('name'),
                'tags': quote.get('tags'),
                'quote': quote.get('text'),
            }

        has_next = json_response.get("has_next")
        if has_next:
            next_page = json_response.get("page") + 1
            yield scrapy.Request(
                url=f"https://quotes.toscrape.com/api/quotes?page={next_page}",
                callback=self.parse
            )
