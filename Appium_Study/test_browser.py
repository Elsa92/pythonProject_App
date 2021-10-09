from time import sleep

from appium import webdriver



class TestBrowser:

    def setup(self):
        caps = {
            'platformName': 'Android',
            'deviceName': '127.0.0.1:7555',
            'noReset': 'True',
            # for 默认浏览器
            'browserName': 'Browser',
            # 指定webdriver 存放的路径
            # 'chromedriverExecutable': 'C:/Users/Elsa/Documents'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        sleep(5)

