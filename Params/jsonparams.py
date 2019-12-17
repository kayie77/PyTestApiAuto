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
    # log.info('解析json, Path:' + path_dir + '/Params/Param/Json/' + case_name + '.json')
    data = jsontools.GetPages().get_page_list(case_name)
    param = data[case_name]
    return param


class Basic:
    def __init__(self):
        self.log = Log.MyLog()

    @staticmethod
    def get_case_datas(api_name):
        params = get_parameter('temp')  # 指定读取的json文件名
        case_data = []  # 声明返回数组
        for i in range(0, len(params)):
            if params[i]['request']['description'] == api_name:
                case_dict = {}
                case_dict["name"] = params[i]['request']['description']  # 获取name
                case_dict["url"] = params[i]['request']['url']['raw']   # 获取url
                # 获取header，针对postman格式的解析，所以较为麻烦
                headersDict = {}
                headers = params[i]['request']['header']
                for j in range(0, len(headers)):
                    headersDict[headers[j]["key"]] = headers[j]["value"]
                case_dict["header"] = headersDict
                # 获取body，针对postman格式的解析，所以较为麻烦
                if not params[i]['request']['body'] is None:
                    bodysDict = {}
                    bodys = params[i]['request']['body']['formdata']
                    for k in range(0, len(bodys)):
                        bodysDict[bodys[k]["key"]] = bodys[k]["value"]
                    case_dict["body"] = bodysDict
                # 放入返回数组
                case_data.append(case_dict)
        return case_data