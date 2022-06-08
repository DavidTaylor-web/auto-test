import requests

phone = "13912312345"
nick = "fengluojifan"
passwd = "123456"
#1. 注册账户
url_regis = "http://trip.imooc.zhaedu.com/api/accounts/user/register/"
data_regis = {"username":phone,"nickname":nick,"password":passwd}
res_regis = requests.post(url=url_regis,data=data_regis)
print(res_regis.text)
#2. 登录
url_login = "http://trip.imooc.zhaedu.com/api/accounts/user/login/"
data_login = {"username":phone,"password":passwd}
res_login = requests.post(url=url_login,data=data_login)
print(res_login.text)
cookies = requests.utils.dict_from_cookiejar(res_login.cookies)
print(cookies)
#3. 用户信息查询
url_view = "http://trip.imooc.zhaedu.com/api/accounts/user/detail/"
res_view = requests.get(url=url_view,cookies=cookies)
print(res_view.text)
