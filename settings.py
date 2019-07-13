import logging



# 代理ip默认的最高分
MAX_SCORE = 50

# 日志默认信息
LOG_LEVEL = logging.INFO
LOG_FMT = '%(asctime)s %(filename)s, [line:%(lineno)d] %(levelname)s: %(message)s'
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
LOG_FILENAME = 'log.log'

TIMEOUT = 2

MONGO_URL = 'mongodb://127.0.0.1:27017'


PROXIES_SPIDERS = [
    'core.proxy_spider.proxy_spider.XiciSpider',
    'core.proxy_spider.proxy_spider.CNproxy',
    'core.proxy_spider.proxy_spider.GouBanJia',
    'core.proxy_spider.proxy_spider.Ip3366'

]

# 单位（分钟）爬取代理的时间间隔
RUN_SPIDER_INTERVAL = 1
# 检测代理ip的时间间隔
TEST_PROXIES_INTEEVAL = 1

# 配置获取代理ip最大数量
PROXIES_MAX_COUNT = 1

# 每次从前几个选取
MAX_CHOICE = 3