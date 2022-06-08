from selenium import webdriver
from pages.base_page import BasePage
from time import sleep

class OrderPage(BasePage):
    """
    第二层
    各个页面单独封装成层，页面的元素、操作、流程
    """
    def product(self):
        return self.by_xpath("//*[@id='app']/div[1]/div[4]/div[2]/a[1]")

    def ticket_book(self):
        return self.by_xpath("//*[@id='app']/div[1]/div[5]/div[2]/div[2]/a")

    def book_date(self):
        return self.by_xpath("//*[@id='app']/div[1]/form/div[1]/div[1]/div[2]/div/input")

    def to_order(self):
        return self.by_xpath("//*[@id='app']/div[1]/form/div[4]/div/button")

    def pay_off(self):
        return self.by_xpath("//*[@id='app']/div[1]/form/div/div/button")

    def confirm(self):
        return self.by_xpath("/html/body/div[5]/div[3]/button[2]")

    #下单成功
    def place_order(self):
        self.product().click()
        self.ticket_book().click()
        self.book_date().send_keys("2020-12-09")
        self.to_order().click()
        sleep(2)
        el = self.pay_off()
        self.driver.execute_script('arguments[0].click()',el)
        sleep(2)