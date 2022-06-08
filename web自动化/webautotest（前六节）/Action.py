from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/WEBAUTO/sendkeys.html")
#Action
#key_down 模拟按键按下
# key_up
#click
#send_keys
#double_click
#click_and_hold
#release
#move_to
#content_click
#drag_and_drop
#perform
double_click_el = driver.find_element_by_id('A')
ActionChains(driver).double_click(double_click_el).context_click(double_click_el).perform()
sleep(2)
driver.quit()

