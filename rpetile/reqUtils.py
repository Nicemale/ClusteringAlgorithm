# req Utils
#
import requests
url = "http://www.baidu.com"
response = requests.get(url)

#web的cookie转dict: requests.utils.dict_from_cookiejar()
print("原始cookies:",response.cookies)
print("Utils加工后的cookies:",requests.utils.dict_from_cookiejar(response.cookies))

#将键值对转换为cookiejar: 由于只传入了cookie键值对，会导致部分信息丢失，例如domain...
print(requests.utils.cookiejar_from_dict({'BDORZ': '27315'}))

#util中对url进行编码：会编码冒号、问号、中文字符、等号、连接符号（除英文字符、数字、斜杠外的其它字符)
print(requests.utils.quote(url+"?wd=王进之&stamp=123333"))

#utils中对url进行解码：
print(requests.utils.unquote(requests.utils.quote(url)))
