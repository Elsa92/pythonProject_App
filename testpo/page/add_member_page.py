from appium.webdriver.common.mobileby import MobileBy

from testpo.page.basepage import BasePage
from testpo.page.edit_member_page import EditMemberPage


class AddMemberPage(BasePage):
    _add_manually = (MobileBy.XPATH, '//*[@text = "手动输入添加"]')

    def click_addmember_menual(self):
        # 点击手动添加按钮
        self.find_and_click(*self._add_manually)

        return EditMemberPage(self.driver)


