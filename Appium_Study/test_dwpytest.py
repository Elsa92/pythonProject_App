# encoding: utf-8

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *


class TestDW:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.main.view.MainActivity'
        desired_caps['noReset'] = 'True'
        # desired_caps['dontStopAppOnReset'] = 'True'
        # desired_caps['skipDeviceInitialization '] = 'Ture'
        desired_caps['unicodeKeyBoard'] = 'True'
        desired_caps['resetKeyBoard']='True'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        '''
        1. 打开雪球
        2. 单击搜索输入框
        3. 向搜索输入框里面输入‘阿里巴巴’
        4.在搜索结果里边选择‘阿里巴巴’。并进行点击
        5. 获取这支香港阿里巴巴股价，并判断这只股价的价格<200

        '''
        self.driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert current_price < 200


    def test_attr(self):
        ele = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tv_banner']/android.widget.ViewFlipper/android.widget.LinearLayout/android.widget.TextView")
        search_enabled = ele.is_enabled()
        print(search_enabled)
        print(ele.text)
        print(ele.location)
        print(ele.size)
        if search_enabled == True:
            ele.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            alibaba_ele = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            alibaba_displayed = alibaba_ele.is_displayed()
            if alibaba_displayed == True:
                print('搜索成功')
            else:
                print('搜索失败')

    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1=int(width/2)
        y_start=int(height*0.8)
        y_end = int(height*0.2)
        action.press(x=x1,y=y_start).wait(500).move_to(x=x1,y=y_end).release().perform()

    def test_get_current_price(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        ele = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price = float(ele.text)
        print(f"当前09988对应的股票的价格是：{current_price}")
        expected_price = 150
        assert_that(current_price, close_to(expected_price, expected_price*0.1))

    def test_myinfo(self):
        """
        1. 打开雪球点击我的
        2. 点击登录雪球
        3. 输入用户名和密码
        4. 点击登录


        :return:
        """
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        text_id = 'resourceId("com.xueqiu.android:id/tab_name").text("我的")'
        self.driver.find_element_by_android_uiautomator(text_id).click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录雪球")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('12345')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find_element(self):
        # new UiScrollable(new UiSelector().scrollable(true).instance(0).scrollIntoView(new UiSelector().text("查找的文本").instance(0)))
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("美股笔记").'
                                                        'instance(0));')




if __name__ == '__main__':
    pytest.main()