from appium import webdriver
from time import sleep

#启动参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = '.activities.PeopleActivity'

#声明手机驱动
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#定位到要操作的联系人
driver.find_element_by_id('com.android.contacts:id/cliv_name_textview').click()
sleep(2)
driver.quit()