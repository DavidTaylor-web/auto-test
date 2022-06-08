import unittest
from selenium import webdriver
from time import sleep

from pages.first_page import FirstPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage
from ddt import ddt,data
from xlrd import open_workbook


def getExcelData():
    excelFile = open_workbook("d:/data.xlsx")
    # 获取excel的工作簿
    sheet = excelFile.sheet_by_index(0)
    #获取行数
    rowNumber = sheet.nrows
    dataList = []
    for i in range(1,rowNumber):
        dataList.append(sheet.row_values(i))

    return dataList

@ddt
class TestTravel(unittest.TestCase):
    # 初始化操作 打开浏览器&浏览器设置
    # 最终结束操作 关闭浏览器
    # 用例分为 登录、下单两个部分

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()


    @data(*getExcelData())
    def test_login_ddt(self, data):
        #初始化参数
        username, password = tuple(data)
        #初始化界面
        first_page = FirstPage(driver=self.dr, path="http://django.t.mukewang.com/#/")
        login_page = LoginPage(driver=self.dr)
        order_page = OrderPage(driver=self.dr)
        #跳转登录
        first_page.cross_to_login()
        #登录
        login_page.login(username, password)
        sleep(2)


    def tearDown(self) :
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()
