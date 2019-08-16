# encoding=utf-8
import requests as rq
import json
import sys
class trans:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
                        '':''}
        self.url_langdetect = "https://fanyi.baidu.com/langdetect"
        self.url_trans = "http://fanyi.baidu.com/basetrans"
        pass
    def langDect(self,query_str):
        r = rq.post(self.url_langdetect,headers=self.headers,data={"query":query_str})
        return json.loads(r.content.decode())["lan"]

    def run(self):

        pass

if __name__=="__main__":
    # query_str = sys.argv[1]
    query_str ="hello"
    trans = trans()

    #lang detect:
    to_lang = "zh"
    from_lang = trans.langDect(query_str)
    print(from_lang)

    if from_lang == "zh":
        to_lang = "en"
    post_data = {
        "quert":query_str,
        "from":from_lang,
        "to":to_lang
    }
    r = rq.post(trans.url_trans,data=post_data,headers=trans.headers)
    if len(r.content) == 0:
        ret = "nothing be transed"
    else:
        ret = json.loads(r.content.decode())["trans"][0]["dst"]
    print("trans result is:",ret)
