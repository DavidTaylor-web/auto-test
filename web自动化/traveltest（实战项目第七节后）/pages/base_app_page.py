from appium import webdriver


class BaseAppPage():
    """
    第一层 basepage层 定义一个所有页面都继承的page层
    对se我们要使用的底层方法进行一次封装
    """

    def __init__(self, driver, path=None):
        # 为了方便编写，把driver初始化，后续改回来
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.driver.implicitly_wait(10)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def by_id(self, id):
        return self.driver.find_element_by_id(id)

    def by_classname(self, classname):
        return self.driver.find_element_by_class_name(classname)

    def by_uiautomator(self,uiautomator):
        return self.driver.find_element_by_android_uiautomator(uiautomator)
