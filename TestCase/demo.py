# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/9 12:18'

import requests
import os
import random
import allure
import pytest

from requests_toolbelt import MultipartEncoder
from Params.params import Basic
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


@pytest.allure.feature('基础模块')
class TestBasic:

	@allure.severity('blocker')
	@allure.story('Basic')
	@pytest.mark.filterwarnings("ignore")
	def test_basic_01(self, action):
		"""
			用例描述：未登陆状态下查看基础设置
		"""
		conf = Config()
		data = Basic()
		test = Assert.Assertions()
		request = Request.Request(action)

		req_url = conf.host_debug
		urls = data.url
		# params = data.data
		headers = data.header

		api_url = req_url + urls[0]
		response = request.get_request(api_url, None, headers[0])

		assert test.assert_code(response['code'], 200)
		assert test.assert_body(response['body'], 'code', 1)
		assert test.assert_body(response['body'], 'message', '操作成功')
		assert test.assert_time(response['time_consuming'], 500)
		Consts.RESULT_LIST.append('True')

	def post_request_multipart(url, data, header, file_parm, file):
		if not url.startswith('http://'):
			url = '%s%s' % ('http://', url)
			print(url)
		try:
			if data is None:
				response = requests.post(url=url, headers=header)
			else:
				data[file_parm] = os.path.basename(file), open(file, 'rb')
				enc = MultipartEncoder(
					fields=data,
					boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
				)

				header['Content-Type'] = enc.content_type
				proxies = {"http": "http://127.0.0.1:5555"}
				response = requests.post(url=url, data=enc, headers=header, proxies=proxies)

		except requests.RequestException as e:
			print('%s%s' % ('RequestException url: ', url))
			print(e)
			return ()

		except Exception as e:
			print('%s%s' % ('Exception url: ', url))
			print(e)
			return ()

		# time_consuming为响应时间，单位为毫秒
		time_consuming = response.elapsed.microseconds / 1000
		# time_total为响应时间，单位为秒
		time_total = response.elapsed.total_seconds()
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

		return response_dicts


if __name__ == '__main__':
	tb = TestBasic()
	api_body = {"type": "1", "isGroupInit": "true", "file": "/Users/jiayiwu/project/newman_cms/datas-new/b.xlsx"}
	api_header = {"Content-Type": "application/x-www-form-urlencoded", "debug": "1", "userid": "727"}
	response = tb.post_request_multipart("http://10.34.4.113:8089/v1/groupInit/import", api_body, api_header, "file", api_body["file"])
	print(response)
