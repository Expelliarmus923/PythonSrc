__author__ = 'lulizhou'
#爬知乎
import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
def ungzip(data):
    try:
        print("正在解压--->")
        data=gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未压缩，无需解压')
    return data
def saveFile(data):
    save_path='E:\python\myData\out.txt'
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()
#获取XSRF
def getXSRF(data):
    cer=re.compile('name=\"_xsrf\" value=\"(.*)\"',flags=0)
    strlist=cer.findall(data)
    return strlist[0]
def getVIEWSTATE(data):
    cer=re.compile('name=\"__VIEWSTATE\" value=\"(.*)\"',flags=0)
    strlist=cer.findall(data)
    return strlist[0]
def makeMyOpener(head):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
url = 'http://www.zhihu.com/'
opener=makeMyOpener(header).open(url)
data=opener.read()
data=ungzip(data)
_xsrf=getXSRF(data.decode())

url+="login"
id='1002359548@qq.com'
passwd='121224llz'
postDict={
    '_xsrf':_xsrf,
    'email':id,
    'password':passwd,
    'rememberme':'y'
}
postData=urllib.parse.urlencode(postDict).encode()
opener=makeMyOpener(header).open(url,postData)
data=opener.read()
data=ungzip(data)
print(data.decode())