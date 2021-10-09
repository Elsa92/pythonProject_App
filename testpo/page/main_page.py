from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from testpo.page.addresslist_page import AddressListPage
from testpo.page.basepage import BasePage


class MainPage(BasePage):
    _contact_icon = (MobileBy.XPATH, '//*[@text = "通讯录"]')
    def goto_addresslist(self):
        # click 通讯录按钮
        self.find_and_click(*self._contact_icon)
        return AddressListPage(self.driver)