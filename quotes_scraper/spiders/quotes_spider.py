import scrapy
from quotes_scraper.items import QuotesScraperItem

class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuotesScraperItem()
            item["text"] = quote.css("span.text::text").get()
            item["author"] = quote.css("span small::text").get()
            yield item
