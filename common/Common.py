#coding=utf-8

from common_interface import CommonInterface as C


'''
    参数说明：
    X_Application_id：app_id
    date：X-Request-At
    X-Application-Auth：X_Application_Auth
    
'''

def get_token(self, X_Application_id,date,X_Application_Auth,results=None):
    url = "http://61.160.149.236:10000/qos-api/t1?APP_ID=12345678"
    head = {
        "x-up-calling-line-id": "15366189548",
        "x-forwarded-for": "10.166.27.61",
        "x-Called-Station-id": "test",
        "x-User-Location-Info": "test",
        "X-Rat-Type": "test",
        "X-Application-Auth": X_Application_Auth,
        "X-Request-At": date,
        "X-Application-Id": X_Application_id
    }
    result = C.get(self,url,data=None,headers=head,results=results)
    return result

def check(self,speed_id,X_Application_id,date,X_Application_Auth,results=None):
    url = "http://61.160.149.236:10000/qos-api/speeding?speeed_id=" + speed_id
    head = {
        "X-Request-At": date,
        "X-Application-Id": X_Application_id,
        "X-Application-Auth": X_Application_Auth,
    }
    result = C.get(self,url,headers=head,results=results)
    return result

def speeding(self,X_Application_id,date,X_Application_Auth,security_token,results=None,dst_info="60.174.237.91:242"):
    url = "http://61.160.149.236:10000/qos-api/speeding"
    head = {
        "X-Request-At": date,
        "X-Application-Id": X_Application_id,
        "X-Application-Auth": X_Application_Auth,
    }
    body = {
        "security_token":security_token,
        "dst_info":dst_info,
        "src_info":"test",
        "user_id":'userid',
        "product_id":"12345678",
        "level":"3",
        "max_volume":"1"
    }
    result = C.post(self,url,data=body,headers=head,results=results)
    return result

def delete_speeding(self,speed_id,X_Application_id,date,X_Application_Auth,results=None):
    url = "http://61.160.149.236:10000/qos-api/speeding?speeed_id=" + speed_id
    head = {
        "X-Request-At": date,
        "X-Application-Id": X_Application_id,
        "X-Application-Auth": X_Application_Auth,
    }
    result = C.delete(self,url,headers=head,results=results)
    return result










