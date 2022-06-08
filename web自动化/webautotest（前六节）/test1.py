from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://django.t.mukewang.com/#/")
# 跳转至登录
el =driver.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[3]")
el.click()
sleep(2)
# 登录
el2 = driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[1]/div[2]/div/input")
el2.clear()
sleep(1)
el2.send_keys('13500000001')
sleep(1)
driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[2]/div[2]/div[1]/input").send_keys('Success@2020')
sleep(1)
driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[3]/button").click()
sleep(2)
# 下单
driver.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[1]").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div[1]/div[4]/div[2]/a[1]").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[2]/div[2]/a").click()
sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[1]/div[1]/div[2]/div/input").send_keys('2020-12-01')
driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div[4]/div/button").click()
sleep(2)
# 首次编写
#driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div/div/button").click()  # 报错not clickable
# 通过js定位
el3 = driver.find_element_by_xpath("//*[@id='app']/div[1]/form/div/div/button")
driver.execute_script('arguments[0].click()',el3)
sleep(1)
driver.find_element_by_xpath("/html/body/div[5]/div[3]/button[2]").click()
sleep(1)

# driver.quit()