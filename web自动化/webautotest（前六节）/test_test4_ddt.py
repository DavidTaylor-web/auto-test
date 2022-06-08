import unittest
from selenium import webdriver
from pages.first_page import FirstPage
from pages.login_page import LoginPage
from ddt import ddt, data
from xlrd import open_workbook
from time import sleep


def getExcelTestData():
    openExcelFile = open_workbook("d:/data.xlsx")
    # 打开Excel文件
    getSheet = openExcelFile.sheet_by_index(0)
    # 获取工作表
    rowNumber = getSheet.nrows
    # 获取行数
    dataList = []
    # 数据List
    for i in range(1, rowNumber):
        # 从第二行开始遍历每一行
        dataList.append(getSheet.row_values(i))
        # 把每个单元格的数值存放到dataList中
    return dataList


@ddt
class TestTravel(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    @data(*getExcelTestData())
    def test_order(self, data):
        username, password = tuple(data)
        # 初始化界面
        first_page = FirstPage(driver=self.dr, path="http://django.t.mukewang.com/#/")
        login_page = LoginPage(driver=self.dr)
        # 跳转至登录
        first_page.cross_to_login()
        # 登录
        login_page.login(username, password)
        sleep(3)

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
