from appium import webdriver
from pages.base_app_page import BaseAppPage

class FirstBaiduPage(BaseAppPage):
    """
    第二层
    各个页面单独封装成层，页面的元素、操作、流程
    """
    def confirm_continue(self):
        return self.by_id("com.baidu.searchbox:id/positive_button")

    def close_ad(self):
        return self.by_id("com.baidu.searchbox:id/introduction_login_close_button")

    def click_search(self):
        return self.by_classname("android.widget.TextSwitcher")

    #方法流程
    def go_to_search(self):
        self.confirm_continue().click()
        self.close_ad().click()
        self.click_search().click()

