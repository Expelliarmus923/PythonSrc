__author__ = 'lulizhou'
import hashlib
md5=hashlib.md5()
md5.update("How are you!")
print md5.hexdigest()
