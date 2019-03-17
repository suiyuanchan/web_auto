from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  as EC


class Base(object):
    # 初始化
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # 定位单个元素方法
    def find(self, locator):
        '''
        :param locator: = ("id","kw")
        :return:
        '''
        element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*locator))
        return element

    # 定位多个元素方法
    def finds(self, locator):
        '''
        :param locator: = ("id","kw")
        :return:s
        '''
        elements = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_elements(*locator))
        return elements

    # 输入文本方法
    def send(self, locator, text):
        element = self.find(locator).send_keys(text)

    # 点击方法
    def click(self, locator):
        element = self.find(locator).click()

    # 判断元素是否存在
    def is_element_exist(self,locator):
        try:
            self.find_element(*locator)
            return True
        except:
            return False

    # 判断多个元素是否存在
    def is_elements_exist(self,locator):
        try:

            if self.find_element(*locator):
                return True
        except:
            return False

    def text_in_element(self,locator,text):
        r = WebDriverWait(self.driver,30,1).until(EC.text_to_be_present_in_element(locator,text))
        return r

    def value_in_element(self,locator,text):
        try:
            r = WebDriverWait(self.driver,30,1).until(EC.text_to_be_present_in_element_value(locator,text))
            return r
        except:
            return False
if __name__ == "__main__":
    url = "http://47.104.190.48:8088/zentao/user-login-L3plbnRhby8=.html"
    driver = webdriver.Chrome()
    driver.get(url)
    # 实例化对象
    lo = Base(driver)
    # 定位用户名
    loc1 = ("name", "account")
    lo.send(loc1, "test123")
    # 定位密码
    loc2 = ("name", "password")
    lo.send(loc2, "!@123456")
    # 定位提交
    loc2 = ("id", "submit")

    lo.click(loc2)
    driver.quit(0)
