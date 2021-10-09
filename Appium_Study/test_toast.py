from appium import webdriver


class TestToast:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.touchboarder.android.api.demos'
        desired_caps['appActivity']= 'com.example.android.apis.view.PopupMenu1'
        automationName: 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element_by_xpath('//*[@resource-id="android:id/content"]/android.widget.LinearLayout/android.widget.Button').click()
        self.driver.find_element_by_xpath('//*[@resource-id="android:id/title" and @text="Search"]').click()
        # print(self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text)
        print(self.driver.find_element_by_xpath('//*[contains(@text,"Clicked popup")]').text)
