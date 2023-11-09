from datetime import datetime
import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from typing import Iterable
from pathlib import Path


class BlogSpider(scrapy.Spider):
    name = "blogspider"
    format_time = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    def start_requests(self) -> Iterable[Request]:
        for p in range(1):
            yield scrapy.Request(
                f"https://www.py.cn/kuangjia?p={p + 1}", callback=self.parse
            )

    def parse(self, response):
        for li in response.css("ul.art-r > li"):
            item = BlogItem()
            item.update(
                {
                    "id": li.css("a:nth-child(1)::attr(href)").re_first(r"(\d+).html"),
                    "title": li.css("p.line1 a::text").extract_first(),
                    "url": response.urljoin(
                        li.css("p.line1 a::attr(href)").extract_first()
                    ),
                    "image_urls": [
                        li.css("a:nth-child(1) img::attr(src)").extract_first()
                    ],
                    "images": "",
                    "author": li.css("img.art-header::attr('alt')").extract_first(),
                    "author_avatar": li.css(
                        "img.art-header::attr('src')"
                    ).extract_first(),
                    "view_num": li.css("div.flex-r > div::text")[1].get().strip(),
                }
            )
            yield response.follow(
                item["url"], self.parse_detail, cb_kwargs=dict(item=item)
            )

    def parse_detail(self, response, item):
        item["content"] = "".join(response.css("div.dl-content p").extract())
        yield item


class BlogItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    author = scrapy.Field()
    author_avatar = scrapy.Field()
    view_num = scrapy.Field()
    content = scrapy.Field()


process = CrawlerProcess(
    settings={
        "ITEM_PIPELINES": {
            "scrapy.pipelines.images.ImagesPipeline": 1,
            "scrapy.pipelines.files.FilesPipeline": 1,
        },
        "IMAGES_STORE": "./output/images",
        "FILES_STORE": "./output/files",
        "FEED_EXPORT_ENCODING": "utf-8",
        "FEEDS": {
            "./output/%(name)s_%(format_time)s.json": {"format": "json"},
        },
    }
)

process.crawl(BlogSpider)
process.start()  # the script will block here until the crawling is finished
