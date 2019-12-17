# coding=utf-8
__author__ = 'wujiayi'
__time__ = '2019/10/10 10:13'

"""
运行用例集：
    python3 run.py
# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""
import pytest
import os

from Common import Log
from Common import Shell
from Conf import Config
import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    # 初始化
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)
    shell = Shell.Shell()
    # 获取报告输出位置
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path
    # 定义测试集
    dir = os.path.split(os.path.abspath(__file__))[0]
    test_case_path = dir + '/TestCase/test_init.py'
    args = ['-s', '-q', '--alluredir', xml_report_path]
    # args.append(test_case_path)
    # 运行命令
    pytest.main(args)
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
