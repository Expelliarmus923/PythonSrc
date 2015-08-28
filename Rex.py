#-*-coding:utf-8-*-
__author__ = 'lulizhou'
import re
if re.match(r'^\d{3}\-\d{3,8}$','210-1234'):
    print 'OK!'
else:
    print "Erro"
#切分字符串
print re.split(r'[\s\,\;]+', 'a,b;; c  d')
#验证Email版本一
#someone@gmail.com
#bill.gates@microsoft.com

email1=re.match(r'^[\w(.?)]+@[\w]+.[\w]+$',"bil.gates@microsoft.com")
print email1