import unittest
from selenium import webdriver
import time


class TestAdd(unittest.TestCase):

    # def tearDown(self):
    #     self.driver.quit()
    #
    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.get("https://www.baidu.com")
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        # 数据准备
        self.driver.get("https://www.baidu.com")
        time.sleep(2)

    def tearDown(self):
        # 数据清理
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_03(self):
        self.driver.find_element_by_id("kw").send_keys("hao")
        # 断言暂时不写
        self.assertTrue(1==2)  # 失败


    def test_02(self):
        self.driver.find_element_by_id("kw").send_keys("ok")
        # 断言暂时不写

if __name__ == '__main__':
    unittest.main()


