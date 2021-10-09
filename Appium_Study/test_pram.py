import pytest
import yaml
from appium import webdriver
from hamcrest import *


class TestPram:

    def setup(self):
        caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.main.view.MainActivity',
            'noReset': 'True',
            'unicodeKeyBoard': 'True',
            'resetKeyBoard': 'True'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/action_close').click()

    @pytest.mark.parametrize('keyword,type,expected_price',yaml.safe_load(open('./data.yml')))
    def test_pram(self,keyword,type,expected_price):
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/tv_banner"]/android.widget.ViewFlipper/android.widget.LinearLayout/android.widget.TextView').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys(keyword)
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name"]').click()
        ele = self.driver.find_element_by_xpath(f'//*[@text="{type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        current_price = float(ele.text)
        print(f"当前这支股票的价格为：{current_price}")
        # expected_price = 150
        assert_that(current_price,close_to(expected_price,expected_price*0.1))


