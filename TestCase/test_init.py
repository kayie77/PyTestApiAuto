# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/9 12:18'

import allure
import pytest

from Params.jsonparams import Basic
from Common import Request
from Common import Consts
from Common import Assert
import Common.Consts

data = Basic()
test = Assert.Assertions()


@pytest.allure.feature('初始化数据模块')
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
		api_url = get_project_list["url"]
		api_header = get_project_list["header"]
		response = request.get_request(api_url, None, api_header)

		assert test.assert_code(response['code'], 200)
		assert test.assert_body(response['body'], 'code', 1)
		assert test.assert_body(response['body'], 'message', '操作成功')
		assert test.assert_time(response['time_consuming'], 500)
		Consts.RESULT_LIST.append('True')

	@allure.story('import_org')
	@pytest.mark.filterwarnings("ignore")
	@pytest.mark.parametrize("import_org", data.get_case_datas("import_org"))
	def test_import_org(self, import_org, action):
		"""
		:param import_org: 导入组织
		:param action: 环境参数
		:return:
		"""
		request = Request.Request(action)
		api_url = import_org["url"]	 # 获取请求地址
		api_header = import_org["header"]	 # 获取请求头
		api_body = import_org["body"]	 # 获取请求体
		response = request.post_request_multipart(api_url, api_body, api_header, "file", Common.Consts.ADMIN_NAME)	 # 发送请求

		assert test.assert_code(response['code'], 200)
		assert test.assert_body(response['body'], 'code', 1)
		assert test.assert_body(response['body'], 'message', '操作成功')
		assert test.assert_time(response['time_consuming'], 500)
		Consts.RESULT_LIST.append('True')

	@allure.story('import_license')
	@pytest.mark.filterwarnings("ignore")
	@pytest.mark.parametrize("import_license", data.get_case_datas("import_license"))
	def test_import_license(self, import_license, action):
		"""
		:param import_license: 导入合同主体
		:param action: 环境参数
		:return:
		"""
		request = Request.Request(action)
		api_url = import_license["url"]	 # 获取请求地址
		api_header = import_license["header"]	 # 获取请求头
		api_body = import_license["body"]	 # 获取请求体
		response = request.post_request_multipart(api_url, api_body, api_header, "file", Common.Consts.ADMIN_NAME)	 # 发送请求

		assert test.assert_code(response['code'], 200)
		assert test.assert_body(response['body'], 'code', 1)
		assert test.assert_body(response['body'], 'message', '操作成功')
		assert test.assert_time(response['time_consuming'], 500)
		Consts.RESULT_LIST.append('True')

	@allure.story('import_user')
	@pytest.mark.filterwarnings("ignore")
	@pytest.mark.parametrize("import_user", data.get_case_datas("import_user"))
	def test_import_user(self, import_user, action):
		"""
		:param import_user: 导入用户
		:param action: 环境参数
		:return:
		"""
		request = Request.Request(action)
		api_url = import_user["url"]	 # 获取请求地址
		api_header = import_user["header"]	 # 获取请求头
		api_body = import_user["body"]	 # 获取请求体
		response = request.post_request_multipart(api_url, api_body, api_header, "file", Common.Consts.ADMIN_NAME)	 # 发送请求

		assert test.assert_code(response['code'], 200)
		assert test.assert_body(response['body'], 'code', 1)
		assert test.assert_body(response['body'], 'message', '操作成功')
		assert test.assert_time(response['time_consuming'], 500)
		Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
	pytest.main("test_init.py")
