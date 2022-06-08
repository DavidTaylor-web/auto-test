from selenium import webdriver
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    第二层
    各个页面单独封装成层，页面的元素、操作、流程
    """
    def login_username(self):
        return self.by_xpath("//*[@id='app']/div[1]/form/div[1]/div[2]/div/input")

    def login_pass(self):
        return self.by_xpath("//*[@id='app']/div[1]/form/div[2]/div[2]/div/input")

    def login_button(self):
        return self.by_xpath("//*[@id='app']/div[1]/form/div[3]/button")

    #登录
    def login(self,username,password):
        self.login_username().send_keys(username)
        self.login_pass().send_keys(password)
        self.login_button().click()