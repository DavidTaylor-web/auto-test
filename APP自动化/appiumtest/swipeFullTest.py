from appium import webdriver
from time import sleep

#获取页面大小
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)

#向左滑动
def swipeLeft(driver):
    l = getSize(driver)
    x1 = int(l[0]*0.9)
    x2 = int(l[0]*0.1)
    y = int(l[1]*0.5)
    driver.swipe(x1,y,x2,y,500)

#向右滑动
def swipeRight(driver):
    l = getSize(driver)
    x1 = int(l[0]*0.9)
    x2 = int(l[0]*0.1)
    y = int(l[1]*0.5)
    driver.swipe(x2,y,x1,y,500)

#向上滑动
def swipeUp(driver):
    l = getSize(driver)
    y1 = int(l[1]*0.9)
    y2 = int(l[1]*0.1)
    x = int(l[0]*0.5)
    driver.swipe(x,y1,x,y2,500)

#向下滑动
def swipeDown(driver):
    l = getSize(driver)
    y1 = int(l[1]*0.9)
    y2 = int(l[1]*0.1)
    x = int(l[0]*0.5)
    driver.swipe(x,y2,x,y1,500)

def swipeDemo():
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
    print(driver.get_window_size())
    driver.find_element_by_id('com.baidu.searchbox:id/positive_button').click()
    sleep(1)
    #关闭广告
    driver.find_element_by_id('com.baidu.searchbox:id/introduction_login_close_button').click()
    sleep(1)
    swipeUp(driver)
    sleep(1)
    swipeUp(driver)
    sleep(1)
    swipeUp(driver)
    sleep(1)
    swipeUp(driver)
    sleep(2)
    driver.quit()

if __name__ == '__main__':
    swipeDemo()