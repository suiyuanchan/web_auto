from common.base import  Base
from selenium import webdriver

import time

class AddBugPage(Base):
    # 定位元素
    loc_test = ("link text","测试")
    #loc_bug = ("link text","Bug")
    loc_tijiao = ("xpath",".//*[@id='createActionMenu']/a")
    loc_mokuai =("xpath",".//*[@id='module_chosen']/a")
    loc_in = ("xpath",".//*[@id='module_chosen']/div/div/input")
    loc_span =("xpath",".//*[@id='module_chosen']/div/ul/li[1]")
    #loc_span =("xpath",".//*[@id='module_chosen']/a/span")
    #loc_sha =("xpath",".//*[@id='contactListGroup']/span/a[2]")
    loc_banben = ("xpath",".//*[@id='openedBuild_chosen']/ul")
    loc_truk = ("xpath",".//*[@id='openedBuild_chosen']/div/ul/li[1]")
    loc_title = ("id","title")




    # 正文切换iframe
    frame = ("class name","ke-edit-iframe")
    loc_body = ("class name","article-content")
    loc_bu =("xpath","html/body/p[1]")

    # 切回主页
    loc_save = ("id","submit")
    # 判读元素方法
    loc_res = ("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def add_bug(self,title="测试标题",body="正文"):
        self.click(self.loc_test)
        #self.click(self.loc_bug)
        self.click(self.loc_tijiao)
        self.click(self.loc_mokuai)
        self.click(self.loc_in)
        self.click(self.loc_span)
        #self.click(self.loc_span)
        self.click(self.loc_banben)
        self.click(self.loc_truk)
        self.send(self.loc_title,title)

        #切换iframe
        f = self.find(self.frame)  # element 对象
        self.driver.switch_to_frame(f)
        #self.send(self.loc_body, "正文")
        self.click(self.loc_body)
        self.send(self.loc_bu,body)

        # 切回
        #self.driver.switch_to_window("Top Window")
        #self.driver.switch_to_window()
        self.driver.switch_to_default_content()
        #self.click(self.loc_sha)
        print(self.find(self.loc_save))
        self.click(self.loc_save)

    def get_title_result(self,_text):
        # text为期望的值
        r = self.text_in_element(self.loc_res,_text)
        return r



if __name__ == '__main__':
    url = "http://47.104.190.48:8088/zentao/user-login-L3plbnRhby8=.html"
    driver = webdriver.Firefox()
    driver.get(url)
    from cases.qita.login2 import  Login
    # 实例化对象
    lo = Login(driver)
    # 登陆
    lo.login()

    # 提交bug流程  # 需要切换浏览器的大小才能成功
    bug = AddBugPage(driver)
    bug.add_bug("第一个缺陷","系统缺陷")
    time.sleep(5)
    driver.quit()


