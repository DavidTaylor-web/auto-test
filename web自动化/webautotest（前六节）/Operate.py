from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/WEBAUTO/form.html")

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

driver.quit()

