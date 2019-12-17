# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/9 11:11'

"""
读取yaml测试数据
"""

import json
import os
import os.path


def parse(case_name):
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params/Param/Json'
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        for name in files:
            file_name = name.split(".")
            if file_name[0] == case_name:
                watch_file_path = os.path.join(root, name)
                with open(watch_file_path, 'r') as f:
                    results = json.loads(f.read())
                    pages = results["item"]
        return pages


class GetPages:
    @staticmethod
    def get_page_list(case_name):
        _page_list = {}
        pages = parse(case_name)
        _page_list[case_name] = pages
        return _page_list


if __name__ == '__main__':
    lists = GetPages.get_page_list("temp")

