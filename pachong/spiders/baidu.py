import scrapy
from pachong.items import PachongItem

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]

    def parse(self, response):
        item = PachongItem()
        item['title'] = response.xpath('//*[@id="ul"]/a[1]/text()').extract()[0]
        item['url'] = response.xpath('//*[@id="ul"]/a[1]/@href').extract_first()
        print(item['title'])
        print(item['url'])
        return item

