import unittest
from selenium import webdriver
from time import sleep


class TestTravel(unittest.TestCase):
    # 初始化操作 打开浏览器&浏览器设置
    # 最终结束操作 关闭浏览器
    # 用例分为 登录、下单两个部分
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(10)
        cls.dr.get("http://django.t.mukewang.com/#/")

    def test_a_login(self):
        # 跳转至登录页
        el_mine = self.dr.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[3]")
        el_mine.click()
        sleep(1)
        # 登录
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[1]/div[2]/div/input").send_keys("13500000001")
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[2]/div[2]/div/input").send_keys("Success@2020")
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[3]/button").click()
        sleep(1)
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[1]").click()
        sleep(2)

    def test_b_order(self):
        # 下单操作
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/div[4]/div[2]/a[1]").click()
        sleep(1)
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/div[5]/div[2]/div[2]/a").click()
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[1]/div[1]/div[2]/div/input").send_keys(
            "2020-12-01")
        self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div[4]/div/button").click()
        sleep(1)
        el = self.dr.find_element_by_xpath("//*[@id='app']/div[1]/form/div/div/button")
        self.dr.execute_script('arguments[0].click()', el)
        self.dr.find_element_by_xpath("/html/body/div[5]/div[3]/button[2]").click()
        sleep(2)

    @classmethod
    def tearDownClass(cls) :
        cls.dr.quit()

if __name__ == '__main__':
    unittest.main()
