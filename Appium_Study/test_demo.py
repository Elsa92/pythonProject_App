from time import sleep

from appium import webdriver


# desired_caps={
#     "platformName": "Android",
#     "deviceName": "127.0.0.1:7555",
#     "appPackage": "com.xueqiu.android",
#     "appActivity": ".view.WelcomeActivityAlias",
#     "noReset": True
# }
from appium.webdriver.extensions.android.gsm import GsmCallActions

desired_caps={}
desired_caps['platformName']= 'Android'
desired_caps['platformVersion']='8.0.0'
desired_caps['deviceName']='192.168.115.102:5555'
# desired_caps['appPackage']='com.xueqiu.android'
# desired_caps['appActivity']='.main.view.MainActivity'
# desired_caps['noReset']='True'
# desired_caps['dontStopAppOnReset']='True'
# desired_caps['skipDeviceInitialization ']='Ture'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)

# driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
# driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
# driver.send_sms('5551234567', 'hello')
driver.make_gsm_call('5551234567', GsmCallActions.CALL)

driver.back()
driver.back()

driver.quit()


