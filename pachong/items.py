# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PachongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    url = scrapy.Field()


class PachongItem2(scrapy.Item):
    # 5i5j部分
    apartment = scrapy.Field()
    total_price = scrapy.Field()
    agent = scrapy.Field()

    # 增加下载图片功能
    image_url = scrapy.Field()
    images = scrapy.Field()

    pass


class PachongItem3(scrapy.Item):
    # fang部分
    title = scrapy.Field()
    total_proce = scrapy.Field()
    area = scrapy.Field()


class PachongItem4(scrapy.Item):
    # qfang部分
    title = scrapy.Field()
    price = scrapy.Field()
