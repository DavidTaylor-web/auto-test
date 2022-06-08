import unittest
from test_login_ddt import TestTravel
from HTMLTestReportCN import HTMLTestRunner
from xmlrunner import xmlrunner

suite = unittest.TestSuite()
suite = unittest.TestLoader().loadTestsFromTestCase(TestTravel)

# f = open("result.html","wb")
# HTMLTestRunner(stream=f,title="UI自动化测试报告",description="风落测试").run(suite)
xmlrunner.XMLTestRunner(verbosity=2, output='测试报告').run(suite)