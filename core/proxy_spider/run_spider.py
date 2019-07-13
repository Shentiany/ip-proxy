from settings import PROXIES_SPIDERS
import importlib
from core.proxy_validate.httpbin_validator import check_proxy
from core.db.mongo_pool import MongoPool
from utils.log import logger
import schedule
import time
from settings import RUN_SPIDER_INTERVAL

class RunSpider(object):

    def __init__(self):
        # 创建数据库对象
        self.mongo_pool = MongoPool()

    def get_spider_from_settings(self):
        '''遍历配置信息中的文件信息'''
        for full_class_name in PROXIES_SPIDERS:
            # print()
            module_name, class_name = full_class_name.rsplit('.', maxsplit=1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            spider = cls()
            yield spider


    def run(self):
        spiders = self.get_spider_from_settings()
        try:
            for spider in spiders:
                for proxy in spider.get_proxy():
                    proxy = check_proxy(proxy)
                    print(proxy)
                    if proxy.speed != -1:
                        pass
                        # 将代理ip写入数据库
                        self.mongo_pool.insert_one(proxy)
        except Exception as ex:
            logger.exception(ex)

    @classmethod
    def start(cls):
        rs = RunSpider()
        rs.run()
        schedule.every(RUN_SPIDER_INTERVAL).minutes.do(rs.run)
        while True:
            schedule.run_pending()
            time.sleep(1)



if __name__ == '__main__':
    RunSpider.start()
