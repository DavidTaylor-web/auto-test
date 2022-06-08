from selenium import webdriver


class BasePage():
    """
    第一层
    对Selenium 进行二次封装，定义一个所有页面都继承的 BasePage ，
    封装 Selenium 基本方法 例如：元素定位，元素等待，导航页面 ，
    不需要全部封装，用到多少方法就封装多少方法。
    """

    def __init__(self, driver, path=None):

        # 第一行为了方便base和page层编写
        # self.driver = webdriver.Chrome()
        self.driver = driver
        # 设置全局定位
        self.driver.implicitly_wait(10)
        self.load_page(path)

    def load_page(self, path=None):
        if path is None:
            url = None
        else:
            url = path
        if url is not None:
            self.driver.get(url)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def js_click(self, xpath):
        self.driver.execute_script('arguments[0].click()', self.by_xpath(xpath))
