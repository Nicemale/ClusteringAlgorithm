# using session:

import requests as req
req_url = "http://test.hhzzss.cn"
login_url = "http://test.hhzzss.cn/Login.do"
#参数传递有两种携带方式：  data = {} | params = {}; 前者是post请求携带参数方式，后者则是get方式
r1 = req.post(url=login_url,data={"username":"994886388","pass":"1"})
# print(r1.content.decode().__contains__("超弦。"))

r = req.get(req_url)
print(r.content.decode().__contains__("超弦"))
