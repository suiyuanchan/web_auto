from selenium import webdriver
from common.base import Base
import time


class Login(Base):
    loc_user = ("name", "account")
    loc_pass =("name","password")
    loc_ti =("id","submit")

    # 登陆方法

    def login(self,user="test123", pwd="!@123456"):
        '''
        登陆函数
        :param driver:
        :param user:
        :param pwd:
        :return:
        '''
        # 输入账号
        self.send(self.loc_user,user)
        #elf.driver.find_element_by_name("account").send_keys(user)
        # driver.find_element_by_id("account").send_keys(user)
        # 输入密码
        self.send(self.loc_pass,pwd)
        #self.driver.find_element_by_name("password").send_keys(pwd)
        # 点击登陆
        self.click(self.loc_ti)
        #self.driver.find_element_by_id("submit").click()

# 获取结果方法
    def get_login_res(self):
        res = ""
        try:
            #res = self.driver.find_element_by_css_selector("#userMenu>a").text
            loc_c =("css selector","#userMenu>a")
            res = self.find(loc_c).text
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
    print(res)
    login.qui()
