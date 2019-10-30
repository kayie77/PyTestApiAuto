# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/9 12:18'

import allure
import pytest

from Params.jsonparams import Basic
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert

conf = Config()
data = Basic()
test = Assert.Assertions()
debug_base_url = conf.host_debug


@pytest.allure.feature('test_basic模块')
class TestBasic:

	@pytest.mark.filterwarnings("ignore")
	@allure.severity('blocker')
	@allure.story('get_project_list')
	@pytest.mark.parametrize("get_project_list", data.get_case_datas("get_project_list"))
	def test_get_project_list(self, get_project_list, action):
		"""
		:param get_project_list: 获取项目列表
		:param action: 环境参数
		"""
		request = Request.Request(action)
		# params = data.data
		api_url = debug_base_url + get_project_list["url"]
		api_header = get_project_list["header"]
		response = request.get_request(api_url, None, api_header)

		assert test.assert_code(response['code'], 200)
		assert test.assert_body(response['body'], 'code', 1)
		assert test.assert_body(response['body'], 'message', '操作成功')
		assert test.assert_time(response['time_consuming'], 500)
		Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
	pytest.main("test_base1.py")
