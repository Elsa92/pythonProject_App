from appium import webdriver

from testpo.page.basepage import BasePage
from testpo.page.main_page import MainPage


class App(BasePage):

    def start(self):
    #     启动应用
        if self.driver == None:
            print('driver == None，新启动driver')
            caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:7555',
                'appPackage': 'com.tencent.wework',
                'appActivity': '.launch.LaunchSplashActivity',
                'noReset': 'True',
                'unicodeKeyBoard': 'True',
                'resetKeyBoard': 'True',
                'settings[waitForIdleTimeout]': 0
            }

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self.driver.implicitly_wait(15)

        else:
            print('driver ！=None, 复用diver')
            self.driver.launch_app()
        return self

    def quit(self):
        self.driver.quit()

    def goto_main(self):

        return MainPage(self.driver)
