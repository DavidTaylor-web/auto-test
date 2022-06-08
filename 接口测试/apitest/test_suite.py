import unittest
from test_account import TestAccount
from test_account2 import TestAccount2

suite = unittest.TestSuite()
# suite.addTest(TestAccount('test_login_normal'))
# # suite.addTest(TestAccount2('test_login_wrong2'))
suite.addTests([TestAccount('test_login_normal'),TestAccount2('test_login_wrong2')])

#输出到文本文件中测试结果
with open("result.txt","w") as f:
    unittest.TextTestRunner(stream=f,verbosity=2).run(suite)


