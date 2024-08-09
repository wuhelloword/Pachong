import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pachong.items import PachongItem3


class FangSpider(CrawlSpider):
    name = "fang"
    allowed_domains = ["fang.com"]
    start_urls = ["https://fang.com"]

    # 第一个rule没有设置callback，follow默认true,因此会跟进网页中符合正则表达式提取规则的URL，通过这种跟进，实现对全部二手房列表页面进行爬取
    # 第二个rule当规则匹配成功并请求后，交给callback设置的函数解析出具体信息。因为设置了callback所以不会跟进网页中的url
    rules = (Rule(LinkExtractor(allow=r"https://esf.fang.com/house.*")),
             Rule(LinkExtractor(allow=r"https://esf.fang.com/chushou/.*"), callback="parse_item")
             )


    def parse_item(self, response):
        item = PachongItem3()
        # 提取标题信息
        item['title'] = response.xpath(
            'string(//div[@class="tab-cont clearfix"]/div[1])').extract_first().strip('\r\n')[0].strinp()
        # 提取总价
        item['total_price'] = response.xpath('//div[@class="trl-item_top"]/div[1]/i/text()').extract_first()
        item['area'] = response.xpath('//div/[@class="tt"]/text()').extract()[1]
        return item
