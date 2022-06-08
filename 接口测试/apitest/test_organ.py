import unittest
#Test Fixtures(用例包裹方法)
#按不同作用划分
# setUp/tearDown 每个用例执行前 后 执行一次
# setUpClass/tearDownClass 每个测试类加载前执行一次
# setUpModule / tearDownModule 每个测试模块（python文件）加载前 后 执行一次

def setUpModule():
    print( '~~~~~~~~~~~~~~~~~ setUpModule ~~~~~~~~~~~~~~~~~')

def tearDownModule():
    print( '~~~~~~~~~~~~~~~~~ tearDownModule ~~~~~~~~~~~~~~~~~')

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('~~~~~~~~~~~~~~~~~ setUpClass ~~~~~~~~~~~~~~~~~')

    @classmethod
    def tearDownClass(cls):
        print('~~~~~~~~~~~~~~~~~ tearDownClass ~~~~~~~~~~~~~~~~~')

    def setUp(self):
        print('~~~~~~~~~~~~~~~~~ setUp ~~~~~~~~~~~~~~~~~')

    def tearDown(self):
        print('~~~~~~~~~~~~~~~~~ tearDown ~~~~~~~~~~~~~~~~~')

    def test_a(self):
        print('~~~~~~~~~~~~~~~~~ test_a ~~~~~~~~~~~~~~~~~')

    def test_b(self):
        print('~~~~~~~~~~~~~~~~~ test_b ~~~~~~~~~~~~~~~~~')


class TestClass2(unittest.TestCase):
    def test_class2(self):
        print('~~~~~~~~~~~~~~~~~ test_class2 ~~~~~~~~~~~~~~~~~')


if __name__ == '__main__':
    unittest.main()
