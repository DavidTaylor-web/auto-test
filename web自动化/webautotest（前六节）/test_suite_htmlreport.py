import unittest
from test_test4_ddt import TestTravel
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.TestSuite()
suite = unittest.TestLoader().loadTestsFromTestCase(TestTravel)
f = open("result.html","wb")
HTMLTestRunner(stream=f,title="风落的测试报告",description="太棒了").run(suite)
f.close()


