import unittest
from test_account import TestAccount
from test_account2 import TestAccount2

#suite = unittest.TestSuite()
# suite.addTest(TestAccount('test_login_normal'))
# # suite.addTest(TestAccount2('test_login_wrong2'))
#suite.addTests([TestAccount('test_login_normal'),TestAccount2('test_login_wrong2')])
suite = unittest.defaultTestLoader.discover("./")

unittest.TextTestRunner().run(suite)


