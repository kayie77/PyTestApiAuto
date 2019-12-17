# pytest 完整初始框架
## 封装模块：发送请求、数据自动采集、全局配置、读取数据、接口断言、日志记录、allure报告

一、	前言
本文跟大家介绍的是基于python测试框架pytest 与postman数据自动采集的接口自动化测试实践方案，首先了解下为什么是基于pytest框架而不是使用unitest？网上的对比资料很多，概括起来就是pytest 相较于 unittest 代码更加的简洁和灵活，最为跳跃的一点就是 fixture 机制，并且pytest有很多的第三方插件可以扩展和继承，大家可以深入去查一查。
第二个了解的是为什么要做数据自动采集，做数据驱动很多教程推荐的是将数据写在excel中，然后通过程序去读取。但我更推荐的是通过软件自动采集所需数据，这样可以大大节省手动在excel录入数据的时间。推荐使用postman采集数据，它是一款做开发人手必备的接口调试工具，几乎能发送所有类型的HTPP请求，在打开代理模式以后能够自动抓取pc端浏览器或者APP端请求的接口数据，存储并导出后为json格式的数据源，简单方便。
二、	自动化框架流程
整个代码框架除了数据来源从postman采集，其他所有封装的公共库以及具体的测试用例均使用代码编辑器如pycharm编写python代码，其中需要用到的pytest、requests、allure等库可以直接使用pip命令安装。从数据采集到完成自动化测试并输出测试报告的流程如下图： 
1）	编写公共库：如果某个函数需要被多次引用，那么就可以封装成公共函数，这些封装的函数主要有：断言、全局常量、log日志、发送请求、用户session、加密等。跟业务无关，可以先封装好。
 
2）	编写配置文件：配置文件内容如环境参数、文件存储路径、版本号，以及配置文件的读写封装等，也是编写测试用例之前必须封装好的内容。
 
3）	数据自动采集：如下图所示，打开代理模式，设置代理端口如:5555，设置抓包的存储路径，比如一个功能流程就可以单独存一个集合，最后设置过滤地址为本系统，以免抓到与系统无关的接口 。
 
4）	数据导出json文件存储：选中某个集合后，右键选择export导出，选择第一个json数据格式。导出的数据源放入项目对应的目录Params->json下
 
5）	编写数据读取函数：编写jsonparam.py函数，解析postman格式的json数据。因为postman有些数据不是我们需要的 有些需要拼接，所以需要单独封装一个转换格式的函数，方便测试用例数据读取使用。
 
6）	编写测试用例：在Testcase下编写测试用例的前置和后置参数文件conftest.py文件（此文件名为是固定的，不能写别的）。
 
编写具体的测试用例，测试用例均要使用test开头或结尾（否则框架无法识别）
 
7）	运行测试用例：如果需要运行Testcase下所有测试用例，可以在根目录建run.py文件，若只需要单独运行某个功能的测试用例，也可以在具体的测试文件的main函数里面使用pytest.main("test_xxx.py")命令运行。
 
8）	输出日志文件：过程中使用self.log.info('请求参数：%s' % data)打印日志信息，作为记录和调试使用。
 
9）	输出测试报告：最后可以集成allure插件，输出更加直观漂亮的测试报告。集成过程网上也有很多教程，但是坑非常多，大家需要注意以下内容：
1.建议使用 pytest 3.8.0 版本
命令：pip install pytest
注意：勿使用pytest过高版本，且勿使用allure-pytest插件，会一直报错pytest找不到allure错误，网上的办法也解决不了，亲测使用 pytest 3.8.0 搭配 pytest-allure-adaptor 1.7.10 可以解决
2.建议使用 pytest-allure-adaptor 1.7.10 版本
命令：pip install pytest-allure-adaptor 
3.需要安装jdk 1.8以上版本
4.需要安装 allure-commandline（先安装npm包）
命令：npm install -g allure-commandline --save-dev

接下来按照在run.py文件中写的代码
5.pytest命令基础上加--alluredir，生成xml报告。
pytest -s -q --alluredir [xml_report_path]
6.使用 Command Tool 来生成我们需要的美观报告。
allure generate [xml_report_path] -o [html_report_path]
7.直接用chrome浏览器打开报告，报告会是空白页面
解决办法：在pycharm中右击index.html选择打开方式Open in Browser即可
 
三、	代码结构&源码
 
框架代码分为如下几个模块：Common公共库、Conf配置库、Log封装日志、Params数据源和读取数据、Report测试报告、TestCase测试用例、run.py执行文件，几个重要的函数如下，其他代码已经放到开源github上，大家自行下载。
源码地址：https://github.com/kayie77/PyTestApiAuto
1)	Common->Assert.py 封装断言
直接使用python的assert断言函数，用于判断一个表达式，使用方式：
assert test.assert_code(response['code'], 200)
 
2)	Common->Request.py 封装请求
目的是封装公共请求参数和封装返回内容
 
3)	Conf->Config.py 读取配置文件
在config.ini定义好文件内容，需要再写一个读写配置文件的函数
 
4)	Params->jsonparams.py 读取数据源
Jsonparams的作用是从Postman导出的json数据源中截取所需要的数据，如header、url、body等参数，拼接成requests请求需要的格式返回。
 
 
5)	TestCase->test_xxx.py 测试用例
@allure.story  用于定义被测功能的用户场景，即子功能点
@pytest.mark.parametrize传多个参数，实现执行不同数据
从数据源获取数据后发起请求，断言结果，设置下一接口所需的变量参数
 
6)	run.py 执行文件
获取报告输出位置；定义好需要运行哪些测试集，如果需要全部运行，则不需要定义，会自动找到Test开头（结尾）的包下面test开头（结尾）的py文件；使用pytest.main(args)执行测试用例，定义好allure报告所需参数，使用shell命令生成allure报告
 

