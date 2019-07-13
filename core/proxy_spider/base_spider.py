import requests
from lxml import etree
from utils.http import get_request_headers
from domain import Proxy


class BaseSpider(object):
    urls = []
    group_xpath = ''
    detail_xpath = {}


    def __init__(self, urls=[], group_xpath='', detail_xpath={}):
        if urls:
            self.urls = urls
        if group_xpath:
            self.group_xpath = group_xpath
        if detail_xpath:
            self.detail_xpath = detail_xpath

    def get_page_from_url(self, url):
        response = requests.get(url, headers=get_request_headers())
        return response.content

    def get_first_from_page(self, lis):
        return lis[0] if len(lis) != 0 else ''

    def get_proxies_from_page(self, page):
        element = etree.HTML(page)
        trs = element.xpath(self.group_xpath)
        for tr in trs:
            ip_tmp = tr.xpath(self.detail_xpath['ip'])
            if ':' in ip_tmp:
                ip = ip_tmp.split(':')[0]
            else:
                ip = ip_tmp[0] if ip_tmp else None
            port_tmp = tr.xpath(self.detail_xpath['port'])
            port = port_tmp[0] if port_tmp else None
            area_tmp = tr.xpath(self.detail_xpath['area'])
            area = area_tmp[0] if area_tmp else None
            proxy = Proxy(ip, port, area=area)
            yield proxy

    def get_proxy(self):
        for url in self.urls:
            page = self.get_page_from_url(url)
            proxies = self.get_proxies_from_page(page)
            yield from proxies