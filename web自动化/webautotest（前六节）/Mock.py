from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/WEBAUTO/sendkeys.html")
driver.find_element_by_id('A').send_keys((Keys.CONTROL,'a'))
driver.find_element_by_id('A').send_keys((Keys.CONTROL,'x'))
sleep(2)
driver.find_element_by_id('B').send_keys((Keys.CONTROL,'v'))
sleep(2)
driver.find_element_by_id('B').send_keys((Keys.CONTROL,'a'))
driver.find_element_by_id('B').send_keys((Keys.CONTROL,'c'))
sleep(2)
driver.find_element_by_id('A').send_keys((Keys.CONTROL,'v'))
sleep(2)
driver.quit()

