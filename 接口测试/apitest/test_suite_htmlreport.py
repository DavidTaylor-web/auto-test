import unittest
from test_account import TestAccount
from test_account2 import TestAccount2
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.TestSuite()
# suite.addTest(TestAccount('test_login_normal'))
# # suite.addTest(TestAccount2('test_login_wrong2'))
suite.addTests([TestAccount('test_login_normal'),TestAccount2('test_login_wrong2')])

f = open("result.html","wb")
HTMLTestRunner(stream=f,title="风落的测试报告",description="太棒了").run(suite)
f.close()


