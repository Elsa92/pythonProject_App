from appium import webdriver


class TestClockIn:

    def setup(self):
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

    def teardown(self):
        self.driver.quit()

    def test_clock_in(self):
        self.driver.find_element_by_xpath('//*[@text="工作台"]').click()
        self.driver.find_element_by_xpath('//*[@text="打卡"]').click()
        self.driver.find_element_by_xpath('//*[@text = "外出打卡"]').click()
        self.driver.find_element_by_xpath('//*[contains(@text, "次外出")]').click()
        self.driver.find_element_by_xpath('//*[@text="外出打卡成功"]')


