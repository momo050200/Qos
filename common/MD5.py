#coding=utf-8
import hashlib,time


def MD5():
    X_Application_id = '12345678'

    app_id = 'test'
    date = '2017-11-13T10:59:12Z'

    m2 = hashlib.md5((X_Application_id + app_id + date).encode('utf-8'))

    return m2.hexdigest()



