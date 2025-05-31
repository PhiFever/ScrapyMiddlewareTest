import json
from datetime import datetime
from typing import AsyncIterator, Any

import scrapy


class ScrapyMiddlewareTestSpider(scrapy.Spider):
    name = "ScrapyMiddlewareTest"
    allowed_domains = ["127.0.0.1"]

    async def start(self):
        # 发起第一个请求
        yield scrapy.Request(
            url="http://127.0.0.1:8000/verify",
            method="GET",
            headers={"request_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
            callback=self.parse,
            dont_filter=True,
        )

    def parse(self, response, **kwargs):
        self.logger.info(f'Response : {json.loads(response.text)}')

        # 在这里发起下一个请求，形成持续循环
        yield scrapy.Request(
            url="http://127.0.0.1:8000/verify",
            method="GET",
            headers={"request_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
            callback=self.parse,
            dont_filter=True,
        )
