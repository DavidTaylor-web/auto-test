import unittest
import requests

class TestAccount(unittest.TestCase):

    def test_login_normal(self):
        phone = "13912312345"
        passwd = "123456"
        url_login = "http://trip.imooc.zhaedu.com/api/accounts/user/login/"
        data_login = {"username": phone, "password": passwd}
        res_login = requests.post(url=url_login, data=data_login)
        print(res_login.text)
        self.assertIn("fengluojifan",res_login.text)

    def test_login_wrong(self):
        phone = "13912312345"
        passwd = "123459"
        url_login = "http://trip.imooc.zhaedu.com/api/accounts/user/login/"
        data_login = {"username": phone, "password": passwd}
        res_login = requests.post(url=url_login, data=data_login)
        print(res_login.text)
        self.assertIn("error_code",res_login.text)

if __name__ == '__main__':
    unittest.main()
