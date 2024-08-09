import scrapy
from pachong.items import PachongItem2


class WoaiwojiaAutoParseNextPageSpider(scrapy.Spider):
    name = "woaiwojia_auto_parse_next_page"
    allowed_domains = ["bj.5i5j.com"]

    # 下一页的url可以在parse中构造，然后再继续请求下一页的url，这样start_url中只需要写第一个url
    start_urls = ['https://bj.5i5j.com/ershoufang/n1']


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
        next_url = response.xpath('//div[@class="pageSty rf"]/a[1]/@href').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)   # 网页中解析出的URL经常是不完整的相对路径URL，urljoin方法将其转换为绝对路径的url
            # 使用callback指定parse为回调函数
            yield scrapy.Request(next_url, callback=self.parse)


    def parse_detail(self, response):
        item = response.meta['item']  # 接收传递过来的数据
        # 继续项Item添加经纪人信息
        item['agent'] = response.xpath('//*[@class="dailkansty"]/ul/li[2]/h3/a/text()').extract_first()
        # Images Pipeline用到的是图片的URL列表，所以不需要使用extrac_first()或者列表切片
        item['image_url'] = response.xpath('//*[@class="daikansty"]/ul/li[1]/a/img/@src').extract()
        yield item  # 最后返回Item

