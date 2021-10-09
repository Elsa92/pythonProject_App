from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from wework_testpo.po.basepage import BasePage
from wework_testpo.po.manageaddress_page import ManageAddressPage


class AddressListPage(BasePage):

    # def __init__(self, driver: WebDriver):
    #     # 将上个页面的driver传递过来
    #     self.driver = driver
    _icon= (MobileBy.ID, 'com.tencent.wework:id/j02')

    def goto_manageaddress(self):
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/j02').click()
        self.find_and_click(*self._icon)
        return ManageAddressPage(self.driver)
