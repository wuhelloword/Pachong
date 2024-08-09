import scrapy


class DoubanLoginSpider(scrapy.Spider):
    name = "douban_login"
    allowed_domains = ["douban.com"]
    start_urls = ["https://douban.com/accounts/login"]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'source': 'index_nav', 'form_email': 'a_maybe@163.com', 'form_password': '1234556'},
            callback=self.after_login
        )


    def after_login(self, response):
        author = response.xpath('//*[id="statuses"]/div[2]/div[1]/div/div/div[1]/div[2]/a/text()').extract_first()
        with open('douban.txt', 'wb') as f:
            f.write(response.body)
        return
