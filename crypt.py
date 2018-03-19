# -*- coding:utf-8 -*-

import hashlib
import os

def md5_encrypt(x):

    MD5 = (hashlib.md5(x).hexdigest())

    print(MD5)

    os.remove("./crypt.pyc")

    return MD5
