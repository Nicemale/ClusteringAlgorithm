#取消证书验证\    设置超时参数timeout=10单位秒     通过assert response.status_code == 200判断请求是否成功



import requests as req

url = "http://www.12306.cn"

# 请求证书错误：verify=False
r = req.get(url,verify=False) #如果带https的web请求出现证书错误，使用verify=False可以避免请求失败，可以忽略出现的warning警告
print(r.status_code)
# print(r.content.decode())


#设置超时参数timeout=10单位秒，并进行重试尝试
# from retrying import retry
# @retry(stop_max_attempt_numbers=3) #当下面的方法被捕获到异常就重新执行它(超过3次执行，抛出异常)
r = req.get(url,timeout=2)

#

