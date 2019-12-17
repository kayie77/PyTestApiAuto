# coding=utf-8
__author__ = 'jiayiwu'
__time__ = '2019/11/15 11:16 上午'

import Common.Consts
from Common import Log
from Conf.Config import Config
conf = Config()


class Session:

	@staticmethod
	def get_requests_msg(url, user_type):
		requests_msg = dict()
		if user_type == Common.Consts.ADMIN_NAME:
			debug_split_url = url.split('}}')[1:]
			debug_url = conf.host_debug + debug_split_url[0]

			requests_msg["debug"] = Common.Consts.DEBUG
			requests_msg["userid"] = Common.Consts.ADMIN_ID
			requests_msg["url"] = debug_url
			return requests_msg
		elif user_type == Common.Consts.EXECUTOR_CW_NAME:
			debug_split_url = url.split('}}')[1:]
			debug_url = conf.host_debug + debug_split_url[0]

			requests_msg["debug"] = Common.Consts.DEBUG
			requests_msg["userid"] = Common.Consts.EXECUTOR_CW_ID
			requests_msg["url"] = debug_url
			return requests_msg



