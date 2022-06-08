import unittest
from selenium import webdriver
from time import sleep


class TestTravel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(10)
        cls.dr.get("http://django.t.mukewang.com/#/")

    def test_a_login(self):
        # 跳转至登录
        el = self.dr.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[3]")
        el.click()
        sleep(2)
        # 登录
        el2 = self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[1]/div[2]/div/input")
        el2.clear()
        sleep(1)
        el2.send_keys('13500000001')
        sleep(1)
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[2]/div[2]/div[1]/input").send_keys('Success@2020')
        sleep(1)
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[3]/button").click()
        sleep(2)

    def test_b_order(self):
        # 下单
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[1]").click()
        sleep(2)
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/div[4]/div[2]/a[1]").click()
        sleep(2)
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[2]/div[2]/a").click()
        sleep(2)
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[1]/div[1]/div[2]/div/input").send_keys(
            '2020-12-01')
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[4]/div/button").click()
        sleep(2)
        # 通过js定位
        el3 = self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div/div/button")
        self.dr.execute_script('arguments[0].click()', el3)
        sleep(1)
        self.dr.find_element_by_xpath("/html/body/div[5]/div[3]/button[2]").click()
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main()
