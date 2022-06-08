import unittest

import xmlrunner as xmlrunner

from test_test4_ddt import TestTravel
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.TestSuite()
suite = unittest.TestLoader().loadTestsFromTestCase(TestTravel)

xmlrunner.XMLTestRunner(verbosity=2,output='测试报告').run(suite)


