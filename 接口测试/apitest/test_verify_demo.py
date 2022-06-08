import unittest


class MyTestCase(unittest.TestCase):
    #判断相等
    # def test_equals(self):
    #     # self.assertNotEqual(1, 2/2)
    #     # self.assertListEqual([1,2],[2,1])
    #     # self.assertDictNotEqual({"a":1,"b":2},{"b":2,"a":1})
    #     self.assertIs(1, 2 / 2)

    # #判断是否为空
    # def test_empty(self):
    #     self.assertIsNone("")

    # #判断真假
    # def test_istrue(self):
    #     self.assertFalse(1==2)

    # #是否包含
    # def test_isin(self):
    #     self.assertNotIn("ha","hello")

    # #大小判断
    # def test_greater(self):
    #     self.assertGreaterEqual(3,2)

    #类型判断
    def test_type(self):
        self.assertIsInstance({"a":1},list)
if __name__ == '__main__':
    unittest.main()
