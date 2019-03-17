from selenium import webdriver
import time


class Login(object):
    # 初始化方法
    def __init__(self, driver: webdriver.Chrome):  # 使得driver 是哪个类型，会弹出快捷键
        self.driver = driver

    # 登陆方法

    def login(self, user="test123", pwd="!@123456"):
        '''
        登陆函数
        :param driver:
        :param user:
        :param pwd:
        :return:
        '''
        # 输入账号
        self.driver.find_element_by_name("account").send_keys(user)
        # driver.find_element_by_id("account").send_keys(user)
        # 输入密码
        self.driver.find_element_by_name("password").send_keys(pwd)
        # 点击登陆
        self.driver.find_element_by_id("submit").click()

# 获取结果方法
    def get_login_res(self):
        res = ""
        try:

            res = self.driver.find_element_by_css_selector("#userMenu>a").text
            print("如果成功")
            print("实际结果 %s " % res)
        except:
            res = ""
        return res
    # 退出方法
    def qui(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "http://47.104.190.48:8088/zentao/user-login-L3plbnRhby8=.html"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    login = Login(driver)
    login.login()
    print("over")
    res = login.get_login_res()
    login.qui()
