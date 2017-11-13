#coding=utf-8
import hashlib
import datetime

def MD5():
    X_Application_id = '12345678'
    app_id = 'test'
    date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    m2 = hashlib.md5((X_Application_id + app_id + date).encode('utf-8'))
    X_Application_Auth = m2.hexdigest()
    return X_Application_id,date,X_Application_Auth


if __name__=='__main__':
    print(MD5())



