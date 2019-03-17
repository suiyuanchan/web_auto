import unittest
from selenium import webdriver
from cases.qita.addBugPage2 import AddBugPage
from cases.qita.login2 import Login
import time


class TestAddBug(unittest.TestCase):
    def setUp(self):
        # 打开网站
        self.url = "http://47.104.190.48:8088/zentao/user-login-L3plbnRhby8=.html"
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        lo = Login(self.driver)

        # 实例对象
        self.bug = AddBugPage(self.driver)
        # 登陆
        lo.login()

    def tearDown(self):
        #关闭浏览器
        self.driver.quit()

    # 最核心的代码在封装里，测试只写步骤
    def test_add_bug_01(self):
        '''
        测试数据： title="测试333" ,body="步骤"
        :return:
           self.titel = "测试"+ 时间戳
        '''
        # 如果数据不重复
        title = "测试_%s" % str(time.time())

        # 添加bug
        self.bug.add_bug(title, "步骤")

        # 获取实际结果
        res = self.bug.get_title_result(title)

        # 断言
        self.assertTrue(res)


