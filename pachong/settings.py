# Scrapy settings for pachong project

BOT_NAME = "pachong"

SPIDER_MODULES = ["pachong.spiders"]
NEWSPIDER_MODULE = "pachong.spiders"


# 设置默认用户代理
USER_AGENT = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
]


# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32


# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 10     # 设置下载延时为10秒
# 当设置了download delay，默认会启动RANDOMIZE_DOWNLOAD_DELAY也就是随机等待。当从相同的网站获取数据时，scrapy将会等待一个随机的值（0.5~1.5*DOWNLOAD_DELAY）


# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 设置不启用cookies
COOKIES_ENABLED = False
#

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 这里的优先级没有request中设置的headers优先级高
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
    # "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    #               "AppleWebKit/537.36 (KHTML, like Gecko) "
    #               "Chrome/124.0.0.0 Safari/537.36"
}

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {
   "pachong.middlewares.PachongSpiderMiddleware": 543,
}

# Enable or disable downloader middlewares
# 下载器中间件
DOWNLOADER_MIDDLEWARES = {
    "pachong.middlewares.PachongDownloaderMiddleware": 543,
    "pachong.middlewares.RandomUserAgent": 543,                         # 使用自定义user agent
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,  # 同时需要关闭scrapy默认的user agent
    "pachong.middlewares.MyproxiesSpiderMiddleware": 543,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": None

}
# key中间件类的路径，value中间件的执行顺序，执行顺序的值0~1000整数值

# Enable or disable extensions
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
ITEM_PIPELINES = {
   # "pachong.pipelines.PachongPipeline": 300,
    'scrapy.pipelines.images.ImagesPipeline': 1,        # 启用Image Pipeline
}
IMAGES_STORE = r'C:\Users\F1241948\Desktop\pics'      # 图片储存文件夹

# 自动限速拓展
# 根据scrapy服务器及爬取的网站负载，自动限制爬取速度。使用户不用调节下载延迟及并发请求数来找到优化的值。
AUTOTHROTTLE_ENABLED = True
# 用户只需要指定允许的最大并发请求数，剩下的交给拓展来自动限速拓展完成。
#可设置初始下载延迟和最大下载延时，一般使用默认值即可。

# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False


# Enable and configure HTTP caching (disabled by default)
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

IPPOOL = [
    {'ipaddr': 'http://39.69.15.245:53281'},
    {'ipaddr': 'http://219.138.58.243:3128'}
]
