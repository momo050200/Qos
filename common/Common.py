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
    result = C.get(url,data=None,headers=head)
    return result

def check(self,speed_id,X_Application_id,date,X_Application_Auth):
    url = "http://61.160.149.236:10000/qos-api/speeding?speed_id=" + speed_id
    head = {
        "X-Request-At": date,
        "X-Application-Id": X_Application_id,
        "X_Application_Auth": X_Application_Auth,
    }
    result = C.get(self,url,headers=head)
    return result

def speeding(self,X_Application_id,date,X_Application_Auth,security_token):
    url = "http://61.160.149.236:10000/qos-api/speeding"
    head = {
        "X-Request-At": date,
        "X-Application-Id": X_Application_id,
        "X_Application_Auth": X_Application_Auth,
    }
    body = {
        "security_token":security_token,
        "dst_info":"60.174.237.91:242",
        "src_info":"test",
        "user_id":'userid',
        "product_id":"12345678",
        "level":"3",
        "max_volume":"1"
    }
    result = C.post(self,url,data=body,headers=head)
    return result

def split_speed(self,speed_id,X_Application_id,date,X_Application_Auth):
    url = "http://61.160.149.236:10000/qos-api/speeding?speed_id=" + speed_id
    head = {
        "X-Request-At": date,
        "X-Application-Id": X_Application_id,
        "X_Application_Auth": X_Application_Auth,
    }
    result = C.delete(self,url,headers=head)
    return result










