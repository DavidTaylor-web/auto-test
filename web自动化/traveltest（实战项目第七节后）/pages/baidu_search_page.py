from appium import webdriver
from pages.base_app_page import BaseAppPage

class BaiduSearchPage(BaseAppPage):
    """
    第二层
    各个页面单独封装成层，页面的元素、操作、流程
    """
    def search_input(self):
        return self.by_id("com.baidu.searchbox:id/SearchTextInput")

    def search_button(self):
        return self.by_uiautomator('new UiSelector().resourceId("com.baidu.searchbox:id/float_search_or_cancel")')


    #方法流程
    def content_search(self,content):
        self.search_input().send_keys(content)
        self.search_button().click()

