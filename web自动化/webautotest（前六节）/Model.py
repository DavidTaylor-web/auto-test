from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/WEBAUTO/prompt.html")
#text 返回alert confirm prompt 里边的文字信息
#accept 接受
#dismiss 取消
#send_keys 向prompt里边输入文字
# driver.find_element_by_id('tooltip').click()
# sleep(2)
# alert = driver.switch_to.alert
# print(alert.text)
# sleep(1)
# alert.accept()
# sleep(2)
# sleep(2)
# confirm = driver.switch_to.alert
# print(confirm.text)
# sleep(2)
# confirm.dismiss()
# sleep(2)
# print(confirm.text)
# sleep(2)
# confirm.accept()
# sleep(2)
prompt  = driver.switch_to.alert
print(prompt.text)
sleep(2)
prompt.send_keys('fengluo')
sleep(2)
prompt.accept()
sleep(2)

driver.quit()

