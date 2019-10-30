# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/8 15:47'

from configparser import ConfigParser
from Common import Log
import os


class Config:
	# titles:
	TITLE_DEBUG = "private_debug"
	TITLE_RELEASE = "online_release"
	# values:
	# [debug\release]
	VALUE_TESTER = "tester"
	VALUE_ENVIRONMENT = "environment"
	VALUE_VERSION_CODE = "versionCode"
	VALUE_HOST = "host"
	# path
	path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

	def __init__(self):
		"""
		初始化
		"""
		self.config = ConfigParser()
		self.log = Log.MyLog()
		self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
		self.xml_report_path = Config.path_dir + '/Report/xml'
		self.html_report_path = Config.path_dir + '/Report/html'

		if not os.path.exists(self.conf_path):
			raise FileNotFoundError("请确保配置文件存在！")

		self.config.read(self.conf_path, encoding='utf-8')
		self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
		self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
		self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
		self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)

		self.tester_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_TESTER)
		self.environment_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_ENVIRONMENT)
		self.versionCode_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_VERSION_CODE)
		self.host_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_HOST)

	def get_conf(self, title, value):
		"""
		配置文件读取
		:param title:
		:param value:
		:return:
		"""
		return self.config.get(title, value)

	def set_conf(self, title, value, text):
		"""
		配置文件修改
		:param title:
		:param value:
		:param text:
		:return:
		"""
		self.config.set(title, value, text)
		with open(self.conf_path, "w+") as f:
			return self.config.write(f)

	def add_conf(self, title):
		"""
		配置文件添加
		:param title:
		:return:
		"""
		self.config.add_section(title)
		with open(self.conf_path, "w+") as f:
			return self.config.write(f)
