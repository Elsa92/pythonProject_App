from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from testpo.page.add_member_page import AddMemberPage
from testpo.page.basepage import BasePage


class AddressListPage(BasePage):


    def goto_addmember(self):
        # click 添加成员
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)
