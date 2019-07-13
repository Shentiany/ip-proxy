import requests
import time
import json
from utils.http import get_request_headers
import settings
from domain import Proxy
from utils.log import logger


def check_proxy(proxy):
    """检查代理协议， 匿名程度"""
    proxies = {
        'http':'http://{}:{}'.format(proxy.ip, proxy.port),
        'https':'https://{}:{}'.format(proxy.ip, proxy.port)
    }
    http, http_nick_type, http_speed = __check_http_proxies(proxies)
    https, https_nick_type, https_speed = __check_http_proxies(proxies, False)
    if http and https:
        proxy.protocol = 2
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    elif http:
        proxy.protocol = 0
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    elif https:
        proxy.protocol = 1
        proxy.nick_type = https_nick_type
        proxy.speed = https_speed
    else:
        proxy.protocol = -1
        proxy.nick_type = -1
        proxy.speed = -1


    logger.debug(proxy)
    return proxy

def __check_http_proxies(proxies, is_Http=True):
    nick_type = -1
    speed = -1
    if is_Http:
        test_url = 'http://httpbin.org/get'
    else:
        test_url = 'https://httpbin.org/get'
    try:
        start = time.time()
        response = requests.get(test_url, headers=get_request_headers(), timeout=settings.TIMEOUT, proxies=proxies)
        if response.ok:
            # 计算响应速度
            speed = round(time.time() - start, 2)
            # 把响应内容转化为字典
            content = json.loads(response.text)
            headers = content['headers']
            ip = content['origin']
            proxy_connection = headers.get('Proxy-Connection', None)

            if ',' in ip:
                nick_type = 2
            elif proxy_connection:
                nick_type = 1
            else:
                nick_type = 0
            return True, nick_type, speed
        else:
            return False, nick_type, speed
    except Exception as ex:
        logger.exception(ex)
        return False, nick_type, speed


if __name__ == '__main__':
    proxy = Proxy(ip='203.246.112.133', port='3128')
    print(check_proxy(proxy))
