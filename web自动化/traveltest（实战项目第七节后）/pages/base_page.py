from selenium import webdriver


class BasePage():
    """
    第一层 basepage层 定义一个所有页面都继承的page层
    对se我们要使用的底层方法进行一次封装
    """

    def __init__(self, driver, path=None):
        # 为了方便编写，把driver初始化，后续改回来
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.load_page(path)

    def load_page(self, path=None):
        if path is not None:
            self.driver.get(path)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)


