from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/WEBAUTO/checkbox.html")
#定位所有的checkbox 并勾选
# checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
# for chk in checkboxes:
#     chk.click()

#tag定位
inputs = driver.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
        sleep(1)
sleep(1)

driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
sleep(1)

driver.quit()

