import unittest
from appium import webdriver
from time import sleep

from pages.baidu_search_page import BaiduSearchPage
from pages.first_baidu_page import FirstBaiduPage


class TestLogin(unittest.TestCase):
    # 初始化操作 进行app caps配置
    # 最终结束操作 关闭app

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.baidu.searchbox'
        desired_caps['appActivity'] = 'com.baidu.searchbox.SplashActivity'
        self.dr = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def test_baidu(self):
        # 初始化界面
        first_page = FirstBaiduPage(driver=self.dr)
        search_page = BaiduSearchPage(driver=self.dr)
        # 跳转
        first_page.go_to_search()
        # 搜索
        search_page.content_search("Appium")
        sleep(2)

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
