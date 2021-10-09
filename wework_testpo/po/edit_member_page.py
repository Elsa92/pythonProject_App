from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from wework_testpo.po.basepage import BasePage


class EditMemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     # 将上个页面的driver传递过来
    #     self.driver = driver
    _confirm = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/c10"]')

    def delete_member(self):

        from wework_testpo.po.manageaddress_page import ManageAddressPage
        # ele = self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().text("删除成员").'
        #                                                 'instance(0));')
        # ele.click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/c10"]').click()
        self.swip_and_find('删除成员').click()
        self.find_and_click(*self._confirm)

        return ManageAddressPage(self.driver)