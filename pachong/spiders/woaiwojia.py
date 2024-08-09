import scrapy
from pachong.items import PachongItem2


class WoaiwojiaSpider(scrapy.Spider):
    name = "woaiwojia"
    allowed_domains = ["bj.5i5j.com"]

    start_urls = ['https://bj.5i5j.com/ershoufang/n' + str(i) for i in range(1, 11)]


    def parse(self, response):
        house_list = response.xpath('//*[@class="pList"]/li')
        for house in house_list:
            item = PachongItem2()
            item['apartment'] = house.xpath('div[2]/h3/a/text()').extract_first()
            item['total_price'] = house.xpath('div[2]/div[1]/div/p[1]/strong/text()').extract_first()
            # 解析并构造详情页url
            detail_url = response.urljoin(house.xpath('div[2]/h3/a/@href').extract_first())
            # 继续请求详情页url，使用meta传递已经爬取到的部分数据
            # 使用callback指定回调函数
            yield scrapy.Request(detail_url, meta={'item': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']        # 接收传递过来的数据
        # 继续项Item添加经纪人信息
        item['agent'] = response.xpath('//*[@class="dailkansty"]/ul/li[2]/h3/a/text()').extract_first()
        # Images Pipeline用到的是图片的URL列表，所以不需要使用extrac_first()或者列表切片
        item['image_url'] = response.xpath('//*[@class="daikansty"]/ul/li[1]/a/img/@src').extract()
        yield item  # 最后返回Item
