# coding=utf8

"""
该文件作为 requests_api的配置文件

    作为 api 返回的数据结构为

    response = {
        "status_code": 200,     # 服务器状态码
        ”content“: "xxxx",      # 返回html/json/xml等等
    }
"""

# from __future__ import absolute_import
# import os
import logging

# os.chdir(os.path.split(os.path.abspath(__file__))[0])

# 请求模块日志
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)   # 定义为INFO是因为requests要写debug
request_handler = logging.FileHandler('http_server_log.log')
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
request_handler.setFormatter(fmt)
logger.addHandler(request_handler)

# 定义个过滤器
class RequestFilter(logging.Filter):
    """这是一个过滤request_log的过滤器
    """

    def filter(self, record):
        result = False
        try:
            filter_key = record.isRequest
        except AttributeError:
            filter_key = 'error_record'

        if filter_key == 'notRequestLog':
            result = True
        return result

reqfilter = RequestFilter()
logger.addFilter(reqfilter)

filter_dict = {"isRequest": "notRequestLog"}

# 代理

proxy = {
        "http": "xxxxx",
        "https": "xxxxx",
    }

# 重试次数我

retry = 5

# 请求间隔睡眠时间

r_sleep = 2

# 网页编码

ec_u = 'utf8'

ec_g = 'gbk'