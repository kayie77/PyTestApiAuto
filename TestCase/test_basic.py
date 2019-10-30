# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/9 12:18'

import allure
import pytest

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
