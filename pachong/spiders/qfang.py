from typing import Iterable

import scrapy
from scrapy import Request
from pachong.items import PachongItem4


class QfangSpider(scrapy.Spider):
    name = "qfang"
    allowed_domains = ["m.qfang.com"]
    # start_urls = ["https://m.qfang.com"]

    def parse(self, response):
        house_list = response.xpath('//a')
        for house in house_list:
            item = PachongItem4()
            item['title'] = house.xpath('div[2]/p[1]/text()').extract()[0]
            item['price'] = house.xpath('div[2]/p[3]/em/text()').extract()[0]
            yield item

    def start_requests(self) -> Iterable[Request]:
        # 设置url前面部分
        url_pre = 'http://m.qfang.com/shenzhen/sale?version=a&page='
        for i in range(1, 6):
            url = url_pre + str(i)
            formdata = {'more': str(i)}
            yield scrapy.FormRequest(url, formdata=formdata, callback=self.parse)

