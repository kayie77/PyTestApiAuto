# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/10 10:34'

"""
封装执行shell语句方法
"""
import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o