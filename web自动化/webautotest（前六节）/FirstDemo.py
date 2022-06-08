from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(2)
driver.get("https://www.imooc.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
print('browser will be closed')
driver.quit()




# gecko_driver = "d:\driver\geckodriver.exe"
# driver = webdriver.Firefox(executable_path=gecko_driver)
# driver.get("https://www.baidu.com")

# ie_driver = "d:\driver\IEDriverServer.exe"
# driver = webdriver.Ie(executable_path=ie_driver)
# driver.get("https://www.baidu.com")