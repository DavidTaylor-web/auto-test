from selenium import webdriver
from pages.base_page import BasePage

class FirstPage(BasePage):
    """
    第二层
    各个页面单独封装成层，页面的元素、操作、流程
    """
    def direct_to_login(self):
        return self.by_xpath("//*[@id='app']/div[1]/div[5]/div[3]")

    def direct_to_product(self):
        return self.by_xpath("//*[@id='app']/div[1]/div[5]/div[1]")

    #方法流程
    def cross_to_login(self):
        self.direct_to_login().click()

    def cross_to_product(self):
        self.direct_to_product().click()