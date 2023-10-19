import scrapy
from quotes_scraper.items import QuotesScraperItem

# 改爲繼承 CrawlSpider
class QuotesSpiderLateralSpider(scrapy.Spider):
    name = "quotes_spider_lateral"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuotesScraperItem()
            item["text"] = quote.css("span.text::text").get()
            item["author"] = quote.css("span small::text").get()
            yield item

        # 爬取下一頁
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
