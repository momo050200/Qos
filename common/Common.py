#coding=utf-8

from common_interface import CommonInterface as C


def get_token(self, X_Application_id,date,X_Application_Auth):
    url = "http://61.160.149.236:10000/qos-api/t1?APP_ID=" + X_Application_id
    head = {
        "x-up-calling-line-id": "13390905442",
        "x-forwarded-for": "180.99.55.207",
        "x-Called-Station-id": "test",
        "x-User-Location-Info": "test",
        "X-Rat-Type": "test",
        "X_Application_Auth": X_Application_Auth,
        "X-Request-At": date,
        "X-Application-Id": X_Application_id
    }
    req = C.get(self,url,headers=head)
    # req = urllib.request.Request(url, headers=head)
    # response = urllib.request.urlopen(req)
    # compressedData = eval(response.read().decode())['result']
    # print(type(compressedData))
    # return compressedData
    return req

def check(self,speed_id,X_Application_id,date,X_Application_Auth):
    url = "http://61.160.149.236:10000/qos-api/speeding?speed_id=" + speed_id
    head = {
        "X-Request-At": date,
        "X-Application-Id": X_Application_id,
        "X_Application_Auth": X_Application_Auth,
    }
    result = C.get(self,url,headers=head)


def split_speed(self,speed_id,X_Application_id,date,X_Application_Auth):
    url = "http://61.160.149.236:10000/qos-api/speeding?speed_id=" + speed_id
    head = {
        "X-Request-At": date,
        "X-Application-Id": X_Application_id,
        "X_Application_Auth": X_Application_Auth,
    }
    result = C.delete(self,url,headers=head)










