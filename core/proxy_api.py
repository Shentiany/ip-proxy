from flask import Flask
from flask import request
import json
from core.db.mongo_pool import MongoPool
from settings import PROXIES_MAX_COUNT


class ProxyApi(object):

    def __init__(self):
        self.app = Flask(__name__)
        self.mongo_pool = MongoPool()
        @self.app.route('/random')
        def random():
            protocol = request.args.get('protocol')
            proxy = self.mongo_pool.usable_proxy()
            if protocol:
                return f'{protocol}://{proxy.ip}:{proxy.port}'
            else:
                return f'{proxy.ip}:{proxy.port}'

    def run(self):
        self.app.run('0.0.0.0', port=16888)

    @classmethod
    def start(cls):
        proxy_api = cls()
        proxy_api.run()

if __name__ == '__main__':
    proxy_api = ProxyApi()
    proxy_api.run()