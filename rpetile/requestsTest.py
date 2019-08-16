#使用requests.ger(url)发送请求，获得response
#使用断言判断状态码 assert response.status_code == 200
import requests

# url = "http://www.baidu.com"
# response = requests.get("https://www.baidu.com")
# print(response.status_code)
# assert response.status_code==200

#发送带User-Agent的headers请求：
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

#发送带参数的请求：
# params={"wd":"王进之"}
# url_s = "http://www.baidu.com/s" #这里有无问号无影响
# response = requests.get(url,headers=headers,params=params)


#爬取贴吧前10页的文件到本地
url = "https://tieba.baidu.com/f"
params = {"kw":"李毅","ie":"utf-8","pn":"0"}
for i in range(10):
    r = requests.get(url,headers=headers,params=params)
    params["pn"] = int(params["pn"]) + 50
    with open("./"+str(i)+".html",mode='w',encoding="utf8") as file:
        file.write(r.content.decode())
