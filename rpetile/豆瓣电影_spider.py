#需要使用Referer

import requests
import json
from pprint import pprint

url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=8&loc_id=108288"
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1","Referer":"https://m.douban.com/movie/"}
r = requests.get(url,headers=headers)
resultJson = json.loads(r.content.decode(),encoding="utf-8")
with open("douban.json","w",encoding="utf-8") as f:
    f.write(json.dumps(resultJson,indent=4,ensure_ascii=False))
pprint(resultJson)


with open("douban.json","r",encoding="utf-8") as f:
    doubanJson = json.load(f)
print(doubanJson)

with open("doubanDump.json","w",encoding="utf-8") as f:
    json.dump(doubanJson,f,indent=4,ensure_ascii=False)
