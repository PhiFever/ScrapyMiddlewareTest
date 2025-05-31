import scrapy


class MiddlewareTestSpider(scrapy.Spider):
    name = "middleware_test"
    allowed_domains = ["localhost"]
    start_urls = ["https://localhost"]

    def parse(self, response):
        pass
