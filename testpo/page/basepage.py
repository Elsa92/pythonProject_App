from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    _ADDCONTACT = (MobileBy.XPATH, '//*[@text = "添加成员"]')

    def __init__(self,driver:WebDriver=None):
        self.driver=driver


    def swipe_find(self,text, num=3):

        for i in range(num):
            self.driver.implicitly_wait(1)
            try:
                ele = self.driver.find_element(*self._ADDCONTACT)
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

    def find(self,by,locator):

        return self.driver.find_element(by,locator)

    def find_and_click(self,by,locator):
        self.find(by,locator).click()

    def find_and_sendkeys(self,by, locator,text):
        self.find(by,locator).send_keys(text)

    def get_toast_result(self):
        result = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]').text
        return result

    def back(self, num= 3):
        for i in range(num):
            self.driver.back()



