import requests

# 1 . 组装请求
url = "http://api.tianapi.com/txapi/aqi/index"
data = {"key":"4dce7e012c6391364928602666813641","area":"上海"}

# 2. 发送请求，获取响应
res = requests.post(url=url,data=data)
# 3. 解析响应
print(res.text)