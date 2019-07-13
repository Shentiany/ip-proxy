from settings import MONGO_URL, MAX_CHOICE
from pymongo import MongoClient
from utils.log import logger
from domain import Proxy
import random
import pymongo


class MongoPool(object):

    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.proxies = self.client['proxies_pool']['proxies']

    def __del__(self):
        self.client.close()

    def insert_one(self, proxy):
        count = self.proxies.count_documents({'_id': proxy.ip})
        if count == 0:
            dic = proxy.__dict__
            dic['_id'] = proxy.ip
            self.proxies.insert_one(dic)
            logger.info('插入代理成功')
        else:
            logger.warning('代理已经存在')

    def update_one(self, proxy):
        self.proxies.update_one({'_id': proxy.ip}, {'$set': proxy.__dict__})

    def delete(self, proxy):
        self.proxies.delete({'_id': proxy.ip})
        logger.info(f'删除代理{proxy}')

    def find_all(self):
        cursor = self.proxies.find()
        for item in cursor:
            item.pop('_id')
            proxy = Proxy(**item)
            yield proxy

    def find(self, conditions={}, count=0):
        cursor = self.proxies.find(conditions, limit=count).sort([('score', pymongo.DESCENDING), ('speed', pymongo.ASCENDING)])
        proxy_list = []

        for item in cursor:
            item.pop('_id')
            proxy = Proxy(**item)
            proxy_list.append(proxy)
        return proxy_list

    def usable_proxy(self):
        proxy_list = [self.find()[n] for n in range(MAX_CHOICE)]
        return random.choice(proxy_list)




if __name__ == '__main__':
    mongo = MongoPool()
    for proxy in mongo.find():
        print(proxy)

