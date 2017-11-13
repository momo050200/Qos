#coding=utf-8

import hashlib

def MD5(data):

    m = hashlib.md5(data.encode(encoding='gb2312'))
    Auth = m.hexdigest()
    return Auth


if __name__=='__main__':
    data = '12345678test2017-11-09T01:46:00Z'
    print(MD5(data))
