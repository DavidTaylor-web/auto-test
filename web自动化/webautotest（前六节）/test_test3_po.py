import unittest
from selenium import webdriver
from pages.first_page import FirstPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage


class TestTravel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()

    def test_a_order(self):
        username = '13500000001'
        password = 'Success@2020'
        # 初始化界面
        first_page = FirstPage(driver=self.dr, path="http://django.t.mukewang.com/#/")
        login_page = LoginPage(driver=self.dr)
        order_page = OrderPage(driver=self.dr)
        # 跳转至登录
        first_page.cross_to_login()
        # 登录
        login_page.login(username, password)
        # 跳转至订单页
        first_page.cross_to_order()
        # 下单
        order_page.place_order()

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main()
