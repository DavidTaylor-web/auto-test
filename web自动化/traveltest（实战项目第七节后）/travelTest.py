from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://django.t.mukewang.com/#/")
#跳转至登录页
el_mine = driver.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[3]")
el_mine.click()
sleep(1)
#登录
driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[1]/div[2]/div/input").send_keys("13500000001")
driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[2]/div[2]/div/input").send_keys("Success@2020")
driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[3]/button").click()
sleep(1)
driver.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[1]").click()
sleep(2)
#下单操作
driver.find_element_by_xpath("//*[@id='app']/div[1]/div[4]/div[2]/a[1]").click()
sleep(1)
driver.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[2]/div[2]/a").click()
driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[1]/div[1]/div[2]/div/input").send_keys("2020-12-01")
driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[4]/div/button").click()
sleep(1)
# driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div/div/button").click() # not clickable
el = driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div/div/button")
driver.execute_script('arguments[0].click()', el)
driver.find_element_by_xpath("/html/body/div[5]/div[3]/button[2]").click()
sleep(2)
driver.quit()