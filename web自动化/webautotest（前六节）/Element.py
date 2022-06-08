from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/WEBAUTO/form.html")
# by id
# driver.find_element_by_id('inputEmail').click()
# sleep(1)
# #by name
# driver.find_element_by_name('password').click()
# sleep(1)
# #by tagname
# print(driver.find_element_by_tag_name('form').get_attribute('class'))
# sleep(1)
# #by classname
# el = driver.find_element_by_class_name('controls')
# driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',el)
# sleep(1)
#by linktext
# link = driver.find_element_by_link_text('register')
# driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',link)
# sleep(2)
# partile = driver.find_element_by_partial_link_text('reg')
# driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',partile)
# sleep(3)
# by css selector
# div = driver.find_element_by_css_selector('body > form > div:nth-child(1) > div')
# driver.execute_script('$(arguments[0]).fadeOut().fadeIn()',div)
#by xpath
driver.find_element_by_xpath("/html/body/form/div[3]/div/button").click()
sleep(3)

driver.quit()

