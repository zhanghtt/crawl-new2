# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import redis

SPIDER_MODULES = ['jingdong.spiders']
NEWSPIDER_MODULE = 'jingdong.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = False
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
COOKIES_ENABLED = False

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.


REDIRECT_ENABLED = False

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

REDIS_ITEMS_KEY = '%(spider)s:items'
REDIS_START_URLS_KEY = '%(name)s:start_urls'

REDIS_START_URLS_AS_SET = True
# SCHEDULER_IDLE_BEFORE_CLOSE = 1


# 是否启用扩展，启用扩展为 True， 不启用为 False
MYEXT_ENABLED = True  # 开启扩展
IDLE_TIME = 1800

# 同时扩展里面加入这个
EXTENSIONS = {
    'jingdong.extensions.RedisSpiderClosedExensions': 500,
    'scrapy.telnet.TelnetConsole': None
}
# CLOSESPIDER_TIMEOUT=60
# import scrapy.downloadermiddlewares.defaultheaders
MONGO_URL = "mongodb://192.168.0.13:27017"

LOG_ENABLED = True  # 是否启动日志记录，默认True
# LOG_FILE = 'log.txt'
LOG_LEVEL = 'DEBUG'
LOG_ENCODING = 'UTF-8'
LOG_DATEFORMAT = "%y%y-%m-%d %H:%M:%S"
LOG_FORMAT = '%(asctime)s - %(filename)s -[process:%(processName)s,threadid:%(thread)d]- [line:%(lineno)d] - %(levelname)s: %(message)s'

SPIDER_MIDDLEWARES = {
    "jingdong.spider_middlewares.ExceptionCheckSpider": 501,
}
DOWNLOADER_MIDDLEWARES = {
    "jingdong.downloader_middlewares.CustomHeadersDownLoadMiddleware": 400,
    # "jingdong.downloader_middlewares.ExceptionMiddleware": 999,
    # "jingdong.downloader_middlewares.RetryMiddleware": 550,
    "jingdong.downloader_middlewares.RetryMiddleware": 550,
    'jingdong.downloader_middlewares.ProcessAllExceptionMiddleware': 551,
    'jingdong.downloader_middlewares.DydmicDelayMiddleware': 999,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': None,
    "scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware": 350,
}
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# CONCURRENT_ITEMS = 10
# CONCURRENT_REQUESTS = 10
# CONCURRENT_REQUESTS_PER_DOMAIN = 10
# CONCURRENT_REQUESTS_PER_IP = 10
CONCURRENT_ITEMS = 1
CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

REDIS_START_URLS_BATCH_SIZE=50

RANDOM_DELAY = 0
DOWNLOAD_DELAY = 0
DOWNLOAD_TIMEOUT = 180

DYDMIC_DELAY_ENABLED = True
DYDMIC_DELAY_DEFAULT = 2.5

RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 401]
RETRY_PRIORITY_ADJUST = -1
NEED_SWICH_PROXY = True

DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Connection": "keep-alive"}

# REDIS_URL': 'url',
REDIS_URL = "redis://192.168.0.117:6379/0"

SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

PIPELINE_KEY = '%(spider)s:items'

START_URLS_KEY = '%(name)s:start_urls'
# 自定义
START_URLS_NUM_KEY = "%(name)s:start_urls_num"
RESULT_ITEMS_REDIS_KEY = '%(name)s:items'
HTTP_PROXIES_QUEUE_REDIS_KEY = "%(name)s:http_proxies_queue"
HTTP_PROXIES_ENABELD = False

REDIS_CLS = redis.StrictRedis
REDIS_ENCODING = 'utf-8'
# Sane connection defaults.
REDIS_PARAMS = {
    'socket_timeout': 300,
    'socket_connect_timeout': 300,
    'retry_on_timeout': True,
    'encoding': REDIS_ENCODING,
}

SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

START_URLS_KEY = '%(name)s:start_urls'

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_DEBUG = True
AUTOTHROTTLE_TARGET_CONCURRENCY = 100

DNSCACHE_ENABLED = True
