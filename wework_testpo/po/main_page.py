from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from wework_testpo.po.Addresslist_page import AddressListPage
from wework_testpo.po.basepage import BasePage


class MainPage(BasePage):
    # # 将上一个界面的driver传递过来
    # def __init__(self, driver: WebDriver):
    #     # 将上个页面的driver传递过来
    #     self.driver = driver

    _contact = (MobileBy.XPATH,'//*[@text= "通讯录"]')
    def goto_addresslist(self):
        # #未封装
        # self.find_and_click(MobileBy.XPATH,'//*[@text= "通讯录"]').click()
        # 已封装 #1
        self.find_and_click(*self._contact)


        return AddressListPage(self.driver)