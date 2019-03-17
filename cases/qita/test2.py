import unittest
from selenium import webdriver
from cases.qita.login2 import Login
from cases.qita.addBugPage2 import AddBugPage
class TestAddBug(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://47.104.190.48:8088/zentao/user-login-L3plbnRhby8=.html")
        zen = Login(self.driver)
        self.bug = AddBugPage(self.driver)
        zen.login()  # 登录流程

    def tearDown(self):
        self.driver.quit()

    def test_add_bug_01(self):
        '''测试数据 title="测试333", body="正文33"'''
        import time
        # 如果测试数据不重复
        title = "测试_%s" % str(time.time())
        self.bug.add_bug(title, "正文33")   # 提交BUG流程
        # 获取实际结果
        result = self.bug.get_title_result(title)
        print("获取到的判断结果：%s" % result)
        self.assertTrue(result)



