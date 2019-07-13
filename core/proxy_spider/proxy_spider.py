from core.proxy_spider.base_spider import BaseSpider

class XiciSpider(BaseSpider):
    urls = ['https://www.xicidaili.com/']
    group_xpath = '//table[@id="ip_list"]/tr[@class="odd"]'
    detail_xpath = {
        'ip': './td[2]/text()',
        'port': './td[3]/text()',
        'area': './td[4]/text()'
    }

class CNproxy(BaseSpider):
    urls = ['https://cn-proxy.com/archives/218']
    group_xpath = '//table[@class="sortable"]/tbody/tr'
    detail_xpath = {
        'ip': './td[1]/text()',
        'port': './td[2]/text()',
        'area': './td[3]/text()'
    }

class Jiangxianli(BaseSpider):
    urls = ['http://ip.jiangxianli.com/']
    group_xpath = '//table[@class="table table-hover table-bordered table-striped"]/tbody/tr'
    detail_xpath = {
        'ip': './td[2]/text()',
        'port': './td[3]/text()',
        'area': './td[6]/text()'
    }

class Ip3366(BaseSpider):
    urls = ['https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1']
    group_xpath = '//table[@cellspacing="1"]//tr[position()>2]'
    detail_xpath = {
        'ip': './td[2]/text()',
        'port': './td[3]/text()',
        'area': './td[5]/text()'
    }


if __name__ == '__main__':
    spider = Ip3366()
    for proxy in spider.get_proxy():
        print(proxy)