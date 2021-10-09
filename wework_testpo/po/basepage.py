from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: WebDriver):
        # 将上个页面的driver传递过来
        self.driver = driver

    def find(self,by,value):
        return self.driver.find_element(by,value)

    def find_and_click(self,by,value):
        self.find(by,value).click()

    def swip_and_find(self,text,num=3):
        for i in range(num):

            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                return ele
            except:
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                start_X = width/2
                start_Y = height*0.8
                end_X = start_X
                end_Y = height*0.2
                self.driver.swipe(start_X,start_Y,end_X,end_Y)

            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了 {i+1} 次，未找到")




