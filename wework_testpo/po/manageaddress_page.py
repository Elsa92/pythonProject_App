from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from wework_testpo.po.basepage import BasePage
from wework_testpo.po.edit_member_page import EditMemberPage


class ManageAddressPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     # 将上个页面的driver传递过来
    #     self.driver = driver

    def goto_edit_member(self,username):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text = "Danielle Weaver"]/../../../..//*[@resource-id="com.tencent.wework:id/h_j"]').click()
        self.swip_and_find(username).click()
        return EditMemberPage(self.driver)

    def get_result(self):
        namelist = self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/j8c"]').text
        return namelist
