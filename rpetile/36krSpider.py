#使用正则匹配开头结尾：
import re
import requests
import json

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
           "Cookie": "JSESSIONID=421F70D680796290FB095CC08579CF1E",
           # "If-None-Match": "\"44d9-5899de3c89f00-gzip\"",
           # "Host": "dept7.guat.edu.cn",
           "Connection": "keep-alive",
           "Cache-Control": "max-age=0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,fr;q=0.7",
           "Referer": "http://dept7.guat.edu.cn/info/1021/2003.htm"
           }
# url = "http://dept7.guat.edu.cn/info/1021/2003.htm"
# for i in range(500):
#     url = "http://test.hhzzss.cn/quest/?qid=351"
#     rRead = requests.get(url,headers=headers)
#     # ret = re.findall("<script>window.initialState=(.*?)</script>",r.content.decode())[0]
#     # ret = json.loads(ret)
#     # with open("36kr.json","w",encoding="utf-8") as f:
#     #     json.dump(ret,f,ensure_ascii=False,indent=4)
#
#     # rClickTimes = requests.get("http://dept7.guat.edu.cn/system/resource/code/news/click/dynclicks.jsp?clickid=2003&owner=1294169589&clicktype=wbnews")
#     # print("当前新闻：",re.findall("<TITLE>(.*?)-",rRead.content.decode()),", 点击次数为",rClickTimes.content.decode())
#     url = "http://test.hhzzss.cn/"
#     rRead = requests.get(url)
#     print("当前浏览数为：",re.findall("<span class=\"pull-right view-count\">(.*?)</span>",rRead.content.decode())[0])
#

"""
    ticket req：
"""

# url = "http://dept7.guat.edu.cn/system/dwr/call/plaincall/NewsvoteDWR.getNewsLinkUrl.dwr"
url_vote = "http://dept7.guat.edu.cn/system/resource/code/datainput.jsp?owner=1294169589&e=1&w=1920&h=1080&treeid=1021&refer=&pagename=L2NvbnRlbnQuanNw&newsid=2003"
url_vote2 = "http://dept7.guat.edu.cn/system/resource/code/datainput.jsp?owner=1294169589&e=1&w=1920&h=1080&treeid=1021&refer=&pagename=L2NvbnRlbnQuanNw&newsid=1989"
url_vote3 = "http://dept7.guat.edu.cn/system/resource/code/datainput.jsp?owner=1294169589&e=1&w=1920&h=1080&treeid=1022&refer=&pagename=L2NvbnRlbnQuanNw&newsid=1994"

url_ori = "http://dept7.guat.edu.cn/info/1021/2003.htm"
url_ori2 = "http://dept7.guat.edu.cn/info/1021/1989.htm"
url_ori3 = "http://dept7.guat.edu.cn/info/1022/1994.htm"

url_clc = "http://dept7.guat.edu.cn/system/resource/code/news/click/dynclicks.jsp?clickid=2003&owner=1294169589&clicktype=wbnews"
url_clc2 = "http://dept7.guat.edu.cn/system/resource/code/news/click/dynclicks.jsp?clickid=1989&owner=1294169589&clicktype=wbnews"
url_clc3 = "http://dept7.guat.edu.cn/system/resource/code/news/click/dynclicks.jsp?clickid=1994&owner=1294169589&clicktype=wbnews"

# data = {
#     "callCount":"1",
#     "page":"http://dept7.guat.edu.cn/info/1021/2003.htm",
#     "scriptSessionId":"AADEE900FBCD52CC2498F24422552B11810",
#     "c0-scriptName":"NewsvoteDWR",
#     "c0-methodName":"getNewsLinkUrl",
#     "c0-param1":"string:1294169589",
#     "c0-id":"0",
#     "c0-param0":"number:2003",
#     "c0-param2":"string:vsb",
#     "batchId":"0",
#     "httpSessionId":""
# }
#
# ret = requests.session().post(url,headers=headers,data=data)

for i in range(10000):
    requests.get(url_vote3) #vote
    requests.get(url_vote2)  # vote
    requests.get(url_vote)  # vote
    # rRead = requests.get(url_ori3)
    # rClickTimes = requests.get(url_clc3)
    # print("当前新闻：",re.findall("<TITLE>(.*?)-",rRead.content.decode()),", 点击次数为",rClickTimes.content.decode())

print("end")



