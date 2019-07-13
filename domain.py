from settings import MAX_SCORE


class Proxy(object):

    def __init__(self, ip=None, port=None, protocol=-1, nick_type=-1, speed=-1, area=None, score=MAX_SCORE):
        # 代理的ip地址
        self.ip = ip
        # 代理ip的端口
        self.port = port
        # 代理ip支持的协议类型(http: 0, https: 1, http和https: 2)
        self.protocol = protocol
        # 代理ip的匿名程度(高匿: 0, 匿名: 1, 透明: 2)
        self.nick_type = nick_type
        # 代理ip的响应速度
        self.speed = speed
        # 代理ip所在的地区
        self.area = area
        # 代理ip的评分,用于衡量代理ip的可用性
        self.score = score
        # 不可用的域名列表
        # self.disable_domains = disable_domain

    def __str__(self):
        return str(self.__dict__)
