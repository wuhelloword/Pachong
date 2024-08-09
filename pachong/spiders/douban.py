from typing import Iterable

import scrapy
from scrapy import Request


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://douban.com"]
    cookies = {}
    headers = {}


    def start_requests(self) -> Iterable[Request]:
        """由于需要爬取登录后的douban网站，所以必须重写这个方法，从而实现个人页面的登录爬取"""
        my_url = 'https://www.douban.com/people/xpython/'
        yield scrapy.Request(my_url, cookies=self.cookies, headers=self.headers, callback=self.parse)

    def parse(self, response):
        name = response.xpath('//*[@id=db-usr-profile"]/div[1]/a/img/@alt').extract_first()
        print(name)
        url_home = 'https://www.douban.com/'
        yield scrapy.Request(url_home, cookies=self.cookies, headers=self.headers, callback=self.parse_home)


    def parse_home(self, response):
        author = response.xpath('//*[@id="statuses"]/div[2]/div[1]/div/div[1]/div[2]/a/text()').extract_first()
        print(author)
