# -*- coding:utf-8 -*-
__author__ = 'lulizhou'

import hashlib

md5 = hashlib.md5()

md5.update('559710'.encode('utf-8'))

print(md5.hexdigest())