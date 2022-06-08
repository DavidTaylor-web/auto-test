from appium import webdriver
from time import sleep

#启动参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.baidu.searchbox'
desired_caps['appActivity'] = 'com.baidu.searchbox.SplashActivity'

#声明手机驱动
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#定位元素 (同意激活)
driver.find_element_by_id('com.baidu.searchbox:id/positive_button').click()
sleep(1)
#关闭广告
driver.find_element_by_id('com.baidu.searchbox:id/introduction_login_close_button').click()
sleep(1)
driver.swipe(100,400,100,100,500)
sleep(1)
driver.swipe(100,400,100,100,500)
sleep(1)
driver.swipe(100,400,100,100,500)
sleep(1)
driver.swipe(100,400,100,100,500)
sleep(2)
driver.quit()