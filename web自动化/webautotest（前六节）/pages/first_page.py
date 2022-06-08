from selenium import webdriver

from pages.base_page import BasePage


class FirstPage(BasePage):
    """
    第二层
    """
    def direct_to_login(self):
        return self.by_xpath("//*[@id='app']/div[1]/div[5]/div[3]")

    def direct_to_order(self):
        return self.by_xpath("//*[@id='app']/div[1]/div[5]/div[1]")

    #跳转登录
    def cross_to_login(self):
        self.direct_to_login().click()

    def cross_to_order(self):
        self.direct_to_order().click()