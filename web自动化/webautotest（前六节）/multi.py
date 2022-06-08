from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/WEBAUTO/multi.html")
sleep(3)
first_window = driver.current_window_handle #将首页句柄暂存
driver.find_element_by_link_text('register').click()
sleep(3)
all_window = driver.window_handles #获取所有句柄
for handle in all_window:
    if handle != first_window: #遍历找到不等于首页的
        driver.switch_to.window(handle)
        print('jumping!!')
sleep(1)
driver.find_element_by_id('kw').send_keys('fengluo')
sleep(2)
driver.find_element_by_id('su').click()
sleep(3)
driver.switch_to.window(first_window)
sleep(2)
el =driver.find_element_by_xpath("//*[@id='inputEmail']")
el.send_keys('jackson')
sleep(1)
el.clear()
sleep(1)
el.send_keys('fengluo')
sleep(1)
driver.find_element_by_xpath("//*[@id='inputPassword']").send_keys('123456')
sleep(1)
driver.find_element_by_xpath("/html/body/form/div[3]/div/button").click()
sleep(2)


# driver.quit()

