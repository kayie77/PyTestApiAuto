# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/9 12:07'

"""
定义所有测试数据
"""

import os
from Params import tools
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class Basic:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Basic.yaml')
    params = get_parameter('Basic')
    url = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        header.append(params[i]['header'])