import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from faker import Faker


class TestAddContact:

    def setup_class(self):
        caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.LaunchSplashActivity',
            'noReset': 'True',
            'unicodeKeyBoard': 'True',
            'resetKeyBoard': 'True',
            'settings[waitForIdleTimeout]':0
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self.driver.implicitly_wait(15)

    def swipe_find(self,text, num=3):
        for i in range(num):
            self.driver.implicitly_wait(1)
            try:
                ele = self.driver.find_element(MobileBy.XPATH , '//*[@text = "添加成员"]')
                self.driver.implicitly_wait(5)
                return ele
            except:
                window_size = self.driver.get_window_size()
                width = window_size['width']
                height = window_size['height']
                start_X = width/2
                start_Y = height*0.8
                end_X = start_X
                end_Y = height*0.2
                self.driver.swipe(start_X,start_Y,end_X,end_Y)
            if i == num-1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f'找了{i+1}次，未找到元素')

    def setup(self):
        self.faker = Faker('zh_CN')

    def teardown_class(self):
        self.driver.quit()


    def test_add_contact(self):
        name = self.faker.name()
        phone = self.faker.phone_number()
        self.driver.find_element(MobileBy.XPATH,'//*[@text = "通讯录"]').click()
        # self.driver.find_element_by_xpath('//*[@text = "添加成员"]').click()
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().text("添加成员").'
        #                                                 'instance(0));').click()

        self.swipe_find('添加成员').click()

        self.driver.find_element(MobileBy.XPATH, '//*[@text = "手动输入添加"]').click()
        # self.driver.find_element_by_id('com.tencent.wework:id/bf_').send_keys(name)
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text, "姓名")]/../*[@text = "必填"]').send_keys(name)
        # self.driver.find_element_by_id('com.tencent.wework:id/ge4').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text, "手机")]/..//*[@text = "必填"]').send_keys(phone)
        self.driver.find_element_by_id('com.tencent.wework:id/ana').click()
        result = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
        assert '添加成功' == result

