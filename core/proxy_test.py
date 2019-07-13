from core.db.mongo_pool import MongoPool
from core.proxy_validate.httpbin_validator import check_proxy
from settings import MAX_SCORE, TEST_PROXIES_INTEEVAL
import schedule
import time


class ProxyTester(object):

    def __init__(self):
        self.mongo_pool = MongoPool()

    def run(self):
        proxies = self.mongo_pool.find_all()
        for proxy in proxies:
            proxy = check_proxy(proxy)
            if proxy.speed == -1:
                proxy.score -= 1
                print('降低分数成功！')
                if proxy.score == 0:
                    self.mongo_pool.delete(proxy)
                else:
                    self.mongo_pool.update_one(proxy)
            else:
                proxy.score = MAX_SCORE
                self.mongo_pool.update_one(proxy)

    @classmethod
    def start(cls):
        proxy_tester =cls()
        proxy_tester.run()
        schedule.every(TEST_PROXIES_INTEEVAL).minutes.do(proxy_tester.run)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    pt = ProxyTester()
    pt.run()
    ProxyTester.start()