from appium.webdriver.common.mobileby import MobileBy

from testpo.page.basepage import BasePage


class EditMemberPage(BasePage):
    _input_name = (MobileBy.XPATH, '//*[contains(@text, "姓名")]/../*[@text = "必填"]')
    _input_phone = (MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text = "必填"]')
    _save = (MobileBy.ID, 'com.tencent.wework:id/ana')

    def edit_member(self,name,phone):
        # 输入成员信息

        from testpo.page.add_member_page import AddMemberPage
        # self.driver.find_element_by_id('com.tencent.wework:id/bf_').send_keys(name)
        self.find_and_sendkeys(*self._input_name,name)
        # self.driver.find_element_by_id('com.tencent.wework:id/ge4').send_keys(phone)
        self.find_and_sendkeys(*self._input_phone,phone)
        self.find_and_click(*self._save)

        return AddMemberPage(self.driver)