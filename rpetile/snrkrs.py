# -*- coding: utf-8 -*-

#使用断言判断状态码 assert response.status_code == 200
import requests, json

user_name = "1772071591@qq.com"
user_pwd = "Fdh123456789"

f=open(r'snrkrsCookies.txt','r',encoding="utf-8")#打开所保存的cookies内容文件
cookies={}#初始化cookies字典变量
for line in f.read().split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
           'Content-type':'application/json'}
login_url_static = "https://www.nike.com/static/ed9c7c9561a1818a5b600fe3b42865c"
login_url_event = "https://analytics.nike.com/v1/batch"
login_do_login = "https://unite.nike.com/login?appVersion=623&experienceVersion=521&uxid=com.nike.commerce.snkrs.web&locale=zh_CN&backendEnvironment=identity&browser=Google%20Inc.&os=undefined&mobile=false&native=false&visit=2&visitor=40281e84-abfc-4ca3-947b-12da2724e2fd"
login_get_userService = "https://unite.nike.com/getUserService?appVersion=623&experienceVersion=521&uxid=com.nike.commerce.snkrs.web&locale=zh_CN&backendEnvironment=identity&browser=Google%20Inc.&os=undefined&mobile=false&native=false&visit=1&visitor=40281e84-abfc-4ca3-947b-12da2724e2fd&viewId=unite&atgSync=false"


login_static_payload = {'sensor_data':'7a74G7m23Vrp0o5c9090261.41-1,2,-94,-100,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36,uaend,12147,20030107,zh-CN,Gecko,3,0,0,0,385143,1327539,1080,1880,1080,1920,1080,619,1080,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:0,sc:0,wrc:1,isc:0,vib:1,bat:1,x11:0,x12:1,8323,0.484052490242,782660663769,loc:-1,2,-94,-101,do_en,dm_en,t_en-1,2,-94,-105,-1,2,-94,-102,0,2,1,0,2526,1878,0;1,2,1,0,2502,883,0;-1,2,-94,-108,0,1,33930,-4,0,0,-1;1,2,34060,-4,0,0,-1;2,1,71402,undefined,0,0,-1;3,2,71403,undefined,0,0,-1;4,1,71404,undefined,0,0,-1;5,2,71405,undefined,0,0,-1;-1,2,-94,-110,0,1,252,155,220;1,1,301,157,220;2,1,310,190,230;3,1,415,362,252;4,1,450,315,244;5,1,465,301,242;6,1,477,295,241;7,1,490,294,241;8,1,519,297,236;9,1,578,332,192;10,1,605,349,165;11,1,630,355,159;12,1,634,374,144;13,1,651,390,131;14,1,668,407,117;15,1,684,418,102;16,1,724,454,75;17,1,751,497,71;18,1,810,550,117;19,1,813,560,133;20,1,822,563,143;21,1,863,565,167;22,1,917,564,166;23,1,1103,563,166;24,1,1130,572,157;25,1,1155,590,134;26,1,1157,606,116;27,1,1180,661,80;28,1,1201,705,60;29,1,1224,747,49;30,1,1234,759,49;31,1,1251,770,49;32,1,1267,772,49;33,1,1285,773,49;34,1,1401,773,50;35,1,1419,773,47;36,1,1436,772,45;37,1,1451,772,43;38,1,1468,775,40;39,1,1486,789,32;40,1,1502,799,30;41,1,1518,809,26;42,1,1534,818,22;43,1,1552,825,17;44,1,1568,830,14;45,1,1585,831,13;46,1,1601,832,13;47,1,1617,833,13;48,1,1652,834,13;49,1,1703,835,13;50,1,1847,841,17;51,1,1867,844,17;52,1,1886,846,19;53,1,1900,849,20;54,1,1950,850,20;55,1,1968,849,23;56,1,1984,845,25;57,1,2001,838,29;58,1,2018,833,33;59,1,2036,828,34;60,1,2052,811,37;61,1,2068,733,37;62,1,2085,489,37;63,1,2101,246,40;64,1,2274,114,46;65,1,29244,62,628;66,1,29252,140,617;67,1,29266,212,606;68,1,29284,331,584;69,1,29300,412,564;70,1,29317,437,548;71,1,29333,440,544;72,1,29454,437,544;73,1,29468,435,542;74,1,29484,437,535;75,1,29501,444,526;76,1,29518,455,509;77,1,29533,480,479;78,1,29550,503,441;79,1,29568,523,405;80,1,29583,545,375;81,1,29601,585,322;82,1,29617,619,276;83,1,29633,637,247;84,1,29650,656,216;85,1,29666,661,202;86,1,29683,662,199;87,1,29699,656,199;88,1,29716,648,199;89,1,29733,647,199;90,1,29812,647,198;91,1,29821,650,195;92,1,29834,654,192;93,1,29849,666,180;94,1,29868,686,165;95,1,29884,733,138;96,1,29901,778,112;97,1,29917,814,89;98,1,29933,822,83;99,1,29949,845,59;117,3,30357,856,16,-1;119,4,30420,856,16,-1;120,2,30425,856,16,-1;146,3,30941,834,78,-1;148,4,31036,834,78,-1;149,2,31037,834,78,-1;247,3,33477,1036,371,-1;249,4,33573,1036,371,-1;250,2,33573,1036,371,-1;506,3,70506,887,19,-1;508,4,70580,887,19,-1;509,2,70581,887,19,-1;695,3,209583,499,449,2232;-1,2,-94,-117,-1,2,-94,-111,0,367,-1,-1,-1;-1,2,-94,-109,0,367,-1,-1,-1,-1,-1,-1,-1,-1,-1;-1,2,-94,-114,-1,2,-94,-103,2,3189;3,30354;2,34168;3,70502;2,71925;3,209581;-1,2,-94,-112,https://www.nike.com/cn/launch/t/daybreak-vegas-gold/-1,2,-94,-115,NaN,1923233,0,367,367,0,NaN,209583,0,1565321327538,8,16745,6,696,2790,9,0,209585,2178394,0,3FEEB588E66D3A40B34B3130BFD8559A~-1~YAAQbBLSPJJy12NsAQAAh3RudALAkwr7Iw3N4d/4N2qrTuooGSR9J4jrXzRYCdDSMEeTlKK+68rzUY/6ctPKBjWe3TwNpHt96B7qnr8kTayG8iNy+tWgFHOsyffi9d/z2paGGjJUc81NkBd1sCJNv2HvsV+K23iSiRQ7VdW/Ws7HaF8MjxQfHEcio/EPv7WLEdoUQAtLd4KKnisQ0rTYynw/B8wKUcfM+FW0TFSL1SUJC3uh+0eIx7VY4Qo4mHkHIfCdpRYHSXeEWuoP93fX9rrfKNiVNJl8Eb1gqlJtnNzdftQURyAf6N7xMkgMfQckEIEXvUw9qzIZ6fN1SD1Ocwvtfon+Jv/GWL+L~-1~-1||~-1,33239,288,792832955,30261693-1,2,-94,-106,1,5-1,2,-94,-119,9,11,12,11,14,14,16,13,11,9,10,10,13,263,-1,2,-94,-122,0,0,0,0,1,0,0-1,2,-94,-123,0.3d648a502951,0.f7d7184f66ed1,0.0d64eedfd7483,0.11e8cda7bd9de,0.7d1fbcab5bb5e,0.7ecf1557ea0af,0.ce7ca5ddc50c2,0.da5d650e326c3,0.f84ce337c15f4,0.aa7abbed3fcd;159,120,42,60,50,50,10,47,34,192;6854,8863,3074,3069,3872,3642,747,3656,2655,13831;3FEEB588E66D3A40B34B3130BFD8559A,1565321327538,NlOjQXTJtx,3FEEB588E66D3A40B34B3130BFD8559A1565321327538NlOjQXTJtx,10000,10000,0.3d648a502951,3FEEB588E66D3A40B34B3130BFD8559A1565321327538NlOjQXTJtx100000.3d648a502951,96,60,62,132,25,239,68,19,102,227,101,174,172,184,70,237,200,75,97,240;-1,2,-94,-70,-1752250632;dis;,7,8;true;true;true;-480;true;24;24;true;false;-1-1,2,-94,-80,5047-1,2,-94,-116,1327540-1,2,-94,-118,233841-1,2,-94,-121,;3;9;0'}
login_event_payload = {"batch":[{"event":"ui:interaction:click","properties":{"language":"zh","country":"CN","experienceId":"com.nike.commerce.snkrs.web","mobile":"false","host":"www.nike.com","pathname":"/cn/launch/t/daybreak-vegas-gold/","action":"ui:interaction:click","view":"login","component":"submitButton","model":{"name":"mobileLoginSubmit"}},"context":{"library":{"name":"unite","version":{"experiences":"521","app":"623"}},"locale":"zh_CN","page":{"hash":"","path":"/cn/launch/t/daybreak-vegas-gold/","referrer":"","search":"","title":"Nike Daybreak 'Vegas Gold' 发布日期. CN","url":"www.nike.com"},"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"},"timestamp":"2019-08-09T03:32:17.184Z","anonymousId":"102E0DEDE013FC57618830BB263084AC","userId":"","type":"track"}]}
login_doLogin_payload = {"username":user_name,"password":user_pwd,"client_id":"PbCREuPr3iaFANEDjtiEzXooFl7mXGQ7","ux_id":"com.nike.commerce.snkrs.web","grant_type":"password"}

data_json_static = json.dumps({'sensor_data':'7a74G7m23Vrp0o5c9090261.41-1,2,-94,-100,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36,uaend,12147,20030107,zh-CN,Gecko,3,0,0,0,385143,1327539,1080,1880,1080,1920,1080,619,1080,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:0,sc:0,wrc:1,isc:0,vib:1,bat:1,x11:0,x12:1,8323,0.484052490242,782660663769,loc:-1,2,-94,-101,do_en,dm_en,t_en-1,2,-94,-105,-1,2,-94,-102,0,2,1,0,2526,1878,0;1,2,1,0,2502,883,0;-1,2,-94,-108,0,1,33930,-4,0,0,-1;1,2,34060,-4,0,0,-1;2,1,71402,undefined,0,0,-1;3,2,71403,undefined,0,0,-1;4,1,71404,undefined,0,0,-1;5,2,71405,undefined,0,0,-1;-1,2,-94,-110,0,1,252,155,220;1,1,301,157,220;2,1,310,190,230;3,1,415,362,252;4,1,450,315,244;5,1,465,301,242;6,1,477,295,241;7,1,490,294,241;8,1,519,297,236;9,1,578,332,192;10,1,605,349,165;11,1,630,355,159;12,1,634,374,144;13,1,651,390,131;14,1,668,407,117;15,1,684,418,102;16,1,724,454,75;17,1,751,497,71;18,1,810,550,117;19,1,813,560,133;20,1,822,563,143;21,1,863,565,167;22,1,917,564,166;23,1,1103,563,166;24,1,1130,572,157;25,1,1155,590,134;26,1,1157,606,116;27,1,1180,661,80;28,1,1201,705,60;29,1,1224,747,49;30,1,1234,759,49;31,1,1251,770,49;32,1,1267,772,49;33,1,1285,773,49;34,1,1401,773,50;35,1,1419,773,47;36,1,1436,772,45;37,1,1451,772,43;38,1,1468,775,40;39,1,1486,789,32;40,1,1502,799,30;41,1,1518,809,26;42,1,1534,818,22;43,1,1552,825,17;44,1,1568,830,14;45,1,1585,831,13;46,1,1601,832,13;47,1,1617,833,13;48,1,1652,834,13;49,1,1703,835,13;50,1,1847,841,17;51,1,1867,844,17;52,1,1886,846,19;53,1,1900,849,20;54,1,1950,850,20;55,1,1968,849,23;56,1,1984,845,25;57,1,2001,838,29;58,1,2018,833,33;59,1,2036,828,34;60,1,2052,811,37;61,1,2068,733,37;62,1,2085,489,37;63,1,2101,246,40;64,1,2274,114,46;65,1,29244,62,628;66,1,29252,140,617;67,1,29266,212,606;68,1,29284,331,584;69,1,29300,412,564;70,1,29317,437,548;71,1,29333,440,544;72,1,29454,437,544;73,1,29468,435,542;74,1,29484,437,535;75,1,29501,444,526;76,1,29518,455,509;77,1,29533,480,479;78,1,29550,503,441;79,1,29568,523,405;80,1,29583,545,375;81,1,29601,585,322;82,1,29617,619,276;83,1,29633,637,247;84,1,29650,656,216;85,1,29666,661,202;86,1,29683,662,199;87,1,29699,656,199;88,1,29716,648,199;89,1,29733,647,199;90,1,29812,647,198;91,1,29821,650,195;92,1,29834,654,192;93,1,29849,666,180;94,1,29868,686,165;95,1,29884,733,138;96,1,29901,778,112;97,1,29917,814,89;98,1,29933,822,83;99,1,29949,845,59;117,3,30357,856,16,-1;119,4,30420,856,16,-1;120,2,30425,856,16,-1;146,3,30941,834,78,-1;148,4,31036,834,78,-1;149,2,31037,834,78,-1;247,3,33477,1036,371,-1;249,4,33573,1036,371,-1;250,2,33573,1036,371,-1;506,3,70506,887,19,-1;508,4,70580,887,19,-1;509,2,70581,887,19,-1;695,3,209583,499,449,2232;-1,2,-94,-117,-1,2,-94,-111,0,367,-1,-1,-1;-1,2,-94,-109,0,367,-1,-1,-1,-1,-1,-1,-1,-1,-1;-1,2,-94,-114,-1,2,-94,-103,2,3189;3,30354;2,34168;3,70502;2,71925;3,209581;-1,2,-94,-112,https://www.nike.com/cn/launch/t/daybreak-vegas-gold/-1,2,-94,-115,NaN,1923233,0,367,367,0,NaN,209583,0,1565321327538,8,16745,6,696,2790,9,0,209585,2178394,0,3FEEB588E66D3A40B34B3130BFD8559A~-1~YAAQbBLSPJJy12NsAQAAh3RudALAkwr7Iw3N4d/4N2qrTuooGSR9J4jrXzRYCdDSMEeTlKK+68rzUY/6ctPKBjWe3TwNpHt96B7qnr8kTayG8iNy+tWgFHOsyffi9d/z2paGGjJUc81NkBd1sCJNv2HvsV+K23iSiRQ7VdW/Ws7HaF8MjxQfHEcio/EPv7WLEdoUQAtLd4KKnisQ0rTYynw/B8wKUcfM+FW0TFSL1SUJC3uh+0eIx7VY4Qo4mHkHIfCdpRYHSXeEWuoP93fX9rrfKNiVNJl8Eb1gqlJtnNzdftQURyAf6N7xMkgMfQckEIEXvUw9qzIZ6fN1SD1Ocwvtfon+Jv/GWL+L~-1~-1||~-1,33239,288,792832955,30261693-1,2,-94,-106,1,5-1,2,-94,-119,9,11,12,11,14,14,16,13,11,9,10,10,13,263,-1,2,-94,-122,0,0,0,0,1,0,0-1,2,-94,-123,0.3d648a502951,0.f7d7184f66ed1,0.0d64eedfd7483,0.11e8cda7bd9de,0.7d1fbcab5bb5e,0.7ecf1557ea0af,0.ce7ca5ddc50c2,0.da5d650e326c3,0.f84ce337c15f4,0.aa7abbed3fcd;159,120,42,60,50,50,10,47,34,192;6854,8863,3074,3069,3872,3642,747,3656,2655,13831;3FEEB588E66D3A40B34B3130BFD8559A,1565321327538,NlOjQXTJtx,3FEEB588E66D3A40B34B3130BFD8559A1565321327538NlOjQXTJtx,10000,10000,0.3d648a502951,3FEEB588E66D3A40B34B3130BFD8559A1565321327538NlOjQXTJtx100000.3d648a502951,96,60,62,132,25,239,68,19,102,227,101,174,172,184,70,237,200,75,97,240;-1,2,-94,-70,-1752250632;dis;,7,8;true;true;true;-480;true;24;24;true;false;-1-1,2,-94,-80,5047-1,2,-94,-116,1327540-1,2,-94,-118,233841-1,2,-94,-121,;3;9;0'})  # dumps：将python对象解码为json数据
data_json_event = json.dumps(login_event_payload)
data_json_doLogin = json.dumps(login_doLogin_payload)
print("loginPayload:",data_json_doLogin)
resp_static = requests.post(url=login_url_static,data=data_json_static,headers=headers,cookies=cookies)
resp_event = requests.post(url=login_url_event,data=data_json_event,headers=headers,cookies=cookies)
resp_doLogin = requests.post(url=login_do_login,data=data_json_doLogin,headers=headers,cookies=cookies)
# access_token = json.loads(resp_doLogin.content,encoding="utf-8")['access_token']

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
#            'Content-type':'application/json',
#            'Authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6IjYzMjdkOGU4LWNlNmMtNGI0MC1iYTdmLTRmYmI0OTM4Zjc4NnNpZyJ9.eyJ0cnVzdCI6MTAwLCJpYXQiOjE1NjUzNTY1MTMsImV4cCI6MTU2NTM2MDExMywiaXNzIjoib2F1dGgyYWNjIiwianRpIjoiMDRkOThkMWEtZGM5Yy00MTU5LThiY2EtZDc2YmU4ZDg5MDQ2IiwibGF0IjoxNTY1MzU2NTEzLCJhdWQiOiJjb20ubmlrZS5kaWdpdGFsIiwic3ViIjoiY29tLm5pa2UuY29tbWVyY2Uuc25rcnMud2ViIiwic2J0IjoibmlrZTphcHAiLCJzY3AiOlsiY29tbWVyY2UiXSwicHJuIjoiODIxYThlNTUtOWEzZS00ZjNjLTk4NTMtM2RkMGJmNWNiYWM5IiwicHJ0IjoibmlrZTpwbHVzIn0.AiiGcJ_uIBNiQgvUVnRKFlfgLISa-h5OYmWm2U-m5r6yIGw6fwKDcUYSz5WdosR_0n7EgjbX-ieEpQUAIEiug5hMdHYBMOmJaSlkch2f8VJ5t99j_6PvE7CmzvqvyDzGcZOBpV9RFCRfsGRHZTH_7bQJpojLMkmqK91eom4EiMOna6IMNTi-9K2E5S5H1BFXT_oKRKDNgsn_mR2w3IXjRZyAiBweoRp6gDPOlx_wmqgjYv8NY2J5Imflgz9uObPEDrRLOsv1q4xnpCkXmwM6idbn3RmBVaIlIYQuPW73OlRbSRIatRDV_PgdlZ4SBqt4s2_nSIS5xRZPd_ETIL0Wzg'}
# resp_get_userService = requests.get(url=login_get_userService,headers=headers,cookies=cookies)
print("resp_static:",resp_static.content)
print("resp_event:",resp_event.content)
print("resp_doLogin:",resp_doLogin)
# print("access_token:",json.loads(resp_doLogin.content,encoding="utf-8")['access_token'])
# print("冯大鸿的信息：",resp_get_userService.content)


# url_json = 'http://httpbin.org/post'
# data_json = json.dumps({'sensor_data':'7a74G7m23Vrp0o5c9090261.41-1,2,-94,-100,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36,uaend,12147,20030107,zh-CN,Gecko,3,0,0,0,385143,1327539,1080,1880,1080,1920,1080,619,1080,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:0,sc:0,wrc:1,isc:0,vib:1,bat:1,x11:0,x12:1,8323,0.484052490242,782660663769,loc:-1,2,-94,-101,do_en,dm_en,t_en-1,2,-94,-105,-1,2,-94,-102,0,2,1,0,2526,1878,0;1,2,1,0,2502,883,0;-1,2,-94,-108,0,1,33930,-4,0,0,-1;1,2,34060,-4,0,0,-1;2,1,71402,undefined,0,0,-1;3,2,71403,undefined,0,0,-1;4,1,71404,undefined,0,0,-1;5,2,71405,undefined,0,0,-1;-1,2,-94,-110,0,1,252,155,220;1,1,301,157,220;2,1,310,190,230;3,1,415,362,252;4,1,450,315,244;5,1,465,301,242;6,1,477,295,241;7,1,490,294,241;8,1,519,297,236;9,1,578,332,192;10,1,605,349,165;11,1,630,355,159;12,1,634,374,144;13,1,651,390,131;14,1,668,407,117;15,1,684,418,102;16,1,724,454,75;17,1,751,497,71;18,1,810,550,117;19,1,813,560,133;20,1,822,563,143;21,1,863,565,167;22,1,917,564,166;23,1,1103,563,166;24,1,1130,572,157;25,1,1155,590,134;26,1,1157,606,116;27,1,1180,661,80;28,1,1201,705,60;29,1,1224,747,49;30,1,1234,759,49;31,1,1251,770,49;32,1,1267,772,49;33,1,1285,773,49;34,1,1401,773,50;35,1,1419,773,47;36,1,1436,772,45;37,1,1451,772,43;38,1,1468,775,40;39,1,1486,789,32;40,1,1502,799,30;41,1,1518,809,26;42,1,1534,818,22;43,1,1552,825,17;44,1,1568,830,14;45,1,1585,831,13;46,1,1601,832,13;47,1,1617,833,13;48,1,1652,834,13;49,1,1703,835,13;50,1,1847,841,17;51,1,1867,844,17;52,1,1886,846,19;53,1,1900,849,20;54,1,1950,850,20;55,1,1968,849,23;56,1,1984,845,25;57,1,2001,838,29;58,1,2018,833,33;59,1,2036,828,34;60,1,2052,811,37;61,1,2068,733,37;62,1,2085,489,37;63,1,2101,246,40;64,1,2274,114,46;65,1,29244,62,628;66,1,29252,140,617;67,1,29266,212,606;68,1,29284,331,584;69,1,29300,412,564;70,1,29317,437,548;71,1,29333,440,544;72,1,29454,437,544;73,1,29468,435,542;74,1,29484,437,535;75,1,29501,444,526;76,1,29518,455,509;77,1,29533,480,479;78,1,29550,503,441;79,1,29568,523,405;80,1,29583,545,375;81,1,29601,585,322;82,1,29617,619,276;83,1,29633,637,247;84,1,29650,656,216;85,1,29666,661,202;86,1,29683,662,199;87,1,29699,656,199;88,1,29716,648,199;89,1,29733,647,199;90,1,29812,647,198;91,1,29821,650,195;92,1,29834,654,192;93,1,29849,666,180;94,1,29868,686,165;95,1,29884,733,138;96,1,29901,778,112;97,1,29917,814,89;98,1,29933,822,83;99,1,29949,845,59;117,3,30357,856,16,-1;119,4,30420,856,16,-1;120,2,30425,856,16,-1;146,3,30941,834,78,-1;148,4,31036,834,78,-1;149,2,31037,834,78,-1;247,3,33477,1036,371,-1;249,4,33573,1036,371,-1;250,2,33573,1036,371,-1;506,3,70506,887,19,-1;508,4,70580,887,19,-1;509,2,70581,887,19,-1;695,3,209583,499,449,2232;-1,2,-94,-117,-1,2,-94,-111,0,367,-1,-1,-1;-1,2,-94,-109,0,367,-1,-1,-1,-1,-1,-1,-1,-1,-1;-1,2,-94,-114,-1,2,-94,-103,2,3189;3,30354;2,34168;3,70502;2,71925;3,209581;-1,2,-94,-112,https://www.nike.com/cn/launch/t/daybreak-vegas-gold/-1,2,-94,-115,NaN,1923233,0,367,367,0,NaN,209583,0,1565321327538,8,16745,6,696,2790,9,0,209585,2178394,0,3FEEB588E66D3A40B34B3130BFD8559A~-1~YAAQbBLSPJJy12NsAQAAh3RudALAkwr7Iw3N4d/4N2qrTuooGSR9J4jrXzRYCdDSMEeTlKK+68rzUY/6ctPKBjWe3TwNpHt96B7qnr8kTayG8iNy+tWgFHOsyffi9d/z2paGGjJUc81NkBd1sCJNv2HvsV+K23iSiRQ7VdW/Ws7HaF8MjxQfHEcio/EPv7WLEdoUQAtLd4KKnisQ0rTYynw/B8wKUcfM+FW0TFSL1SUJC3uh+0eIx7VY4Qo4mHkHIfCdpRYHSXeEWuoP93fX9rrfKNiVNJl8Eb1gqlJtnNzdftQURyAf6N7xMkgMfQckEIEXvUw9qzIZ6fN1SD1Ocwvtfon+Jv/GWL+L~-1~-1||~-1,33239,288,792832955,30261693-1,2,-94,-106,1,5-1,2,-94,-119,9,11,12,11,14,14,16,13,11,9,10,10,13,263,-1,2,-94,-122,0,0,0,0,1,0,0-1,2,-94,-123,0.3d648a502951,0.f7d7184f66ed1,0.0d64eedfd7483,0.11e8cda7bd9de,0.7d1fbcab5bb5e,0.7ecf1557ea0af,0.ce7ca5ddc50c2,0.da5d650e326c3,0.f84ce337c15f4,0.aa7abbed3fcd;159,120,42,60,50,50,10,47,34,192;6854,8863,3074,3069,3872,3642,747,3656,2655,13831;3FEEB588E66D3A40B34B3130BFD8559A,1565321327538,NlOjQXTJtx,3FEEB588E66D3A40B34B3130BFD8559A1565321327538NlOjQXTJtx,10000,10000,0.3d648a502951,3FEEB588E66D3A40B34B3130BFD8559A1565321327538NlOjQXTJtx100000.3d648a502951,96,60,62,132,25,239,68,19,102,227,101,174,172,184,70,237,200,75,97,240;-1,2,-94,-70,-1752250632;dis;,7,8;true;true;true;-480;true;24;24;true;false;-1-1,2,-94,-80,5047-1,2,-94,-116,1327540-1,2,-94,-118,233841-1,2,-94,-121,;3;9;0'})  # dumps：将python对象解码为json数据
# r_json = requests.post(url_json, data_json)
# print(r_json)
# print(r_json.text)
# print(r_json.content)