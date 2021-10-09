from appium import webdriver

from wework_testpo.po.main_page import MainPage


class App:
    def start(self):
        if self.driver == None:

            caps= {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:7555',
                'appPackage': 'com.tencent.wework',
                'appActivity':'.launch.WwMainActivity',
                'noReset': 'True',
                'unicodeKeyBoard': 'True',
                'resetKeyBoard': 'True',
                'settings[waitForIdleTimeout]': 0
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()

        return self

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)

    def back(self,num=3):
        for i in range(num):
            self.driver.back()