# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/9 12:07'

"""
定义所有测试数据
"""

import os
from Params import jsontools
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(case_name):
    log.info('解析json, Path:' + path_dir + '/Params/Param/Json/' + case_name + '.json')
    data = jsontools.GetPages().get_page_list(case_name)
    param = data[case_name]
    return param


class Basic:
    def __init__(self):
        self.log = Log.MyLog()

    def get_case_datas(self, api_name):
        params = get_parameter('test3')  # 指定读取的json文件名
        case_data = []  # 声明返回数组
        for i in range(0, len(params)):
            if params[i]['name'] == api_name:
                case_dict = {}
                case_dict["name"] = params[i]['name']  # 获取name
                case_dict["url"] = params[i]['request']['url']['raw']   # 获取url
                # 获取header，针对postman格式的解析，所以较为麻烦
                headersDict = {}
                headers = params[i]['request']['header']
                for j in range(0, len(headers)):
                    headersDict[headers[j]["key"]] = headers[j]["value"]
                case_dict["header"] = headersDict
                # 放入返回数组
                case_data.append(case_dict)
        return case_data