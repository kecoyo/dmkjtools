import os

from scrapy.cmdline import execute

execute(
    ["scrapy", "runspider", os.path.join(os.path.dirname(__file__), "blog_spider.py")]
)
