#coding=utf-8
import hashlib
import datetime
from IniReader import IniReader


def MD5(X_Application_id):
    file_path = '..\common\cfginfo.ini'
    app_security = IniReader(file_path).get_value('MD5', 'app_security')
    # 定义需要进行加密的数据
    # 生成UTC标准时间，格式：2017-11-14T01:02:00Z
    date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    # 对data进行md5加密
    m2 = hashlib.md5((X_Application_id + app_security + date).encode('utf-8'))
    X_Application_Auth = m2.hexdigest()

    return date,X_Application_Auth


if __name__=='__main__':
    print(MD5(X_Application_id='12345678'))



