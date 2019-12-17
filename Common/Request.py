# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/9 14:20'

"""
封装request
"""
import os
import random
import requests
import Common.Consts
from Common.Session import Session
from Common import Log
from requests_toolbelt import MultipartEncoder


class Request:

    def __init__(self, env):
        """
        :param env:
        """
        self.log = Log.MyLog()

    def get_request(self, url, data, header, user_type):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        try:
            requests_msg = Session.get_requests_msg(url, user_type)
            header["debug"] = requests_msg.get("debug")
            header["userid"] = requests_msg.get("userid")
            url = requests_msg.get("url")
            self.log.info('测试地址：%s' % url)
            self.log.info('请求参数：%s' % data)

            if data is None:
                response = requests.get(url=url, headers=header)
            else:
                response = requests.get(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        self.log.info('返回结果：%s' % response_dicts)
        return response_dicts

    def post_request(self, url, data, header, user_type):
        try:
            requests_msg = Session.get_requests_msg(url, user_type)
            header["debug"] = requests_msg.get("debug")
            header["userid"] = requests_msg.get("userid")
            url = requests_msg.get("url")
            self.log.info('测试地址：%s' % url)
            self.log.info('请求参数：%s' % data)

            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                response = requests.post(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000    # time_consuming为响应时间，单位为毫秒
        time_total = response.elapsed.total_seconds()   # time_total为响应时间，单位为秒
        Common.Consts.STRESS_LIST.append(time_consuming)
        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        self.log.info('返回结果：%s' % response_dicts)
        return response_dicts

    def post_request_multipart(self, url, data, header, file_parm, user_type):
        """
        post文件上传请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param user_type:
        :return:
        """
        try:
            requests_msg = Session.get_requests_msg(url, user_type)
            header["debug"] = requests_msg.get("debug")
            header["userid"] = requests_msg.get("userid")
            url = requests_msg.get("url")
            self.log.info('测试地址：%s' % url)
            self.log.info('请求参数：%s' % data)

            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                data[file_parm] = os.path.basename(data["file"]), open(data["file"], 'rb')
                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                # proxies = {"http": "http://127.0.0.1:5555"} , proxies=proxies
                response = requests.post(url=url, data=enc, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000   # time_consuming为响应时间，单位为毫秒
        time_total = response.elapsed.total_seconds()   # time_total为响应时间，单位为秒
        Common.Consts.STRESS_LIST.append(time_consuming)
        response_dicts = dict()
        response_dicts['code'] = response.status_code
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        self.log.info('返回结果：%s' % response_dicts)
        return response_dicts
