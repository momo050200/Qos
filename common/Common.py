#coding=utf-8

from common_interface import CommonInterface as C
from common.MD5 import MD5
import requests
import urllib.request

def header(self,app_id,date,X_Application_Auth):
    header = {
        "X-Request-At": date,
        "X-Application-Id": app_id,
        "X_Application_Auth": X_Application_Auth,
    }
    return header

def get_token(self, app_id,date,X_Application_Auth):
    # date, X_Application_Auth = MD5()
    url = "http://61.160.149.236:10000/qos-api/t1?APP_ID=" + app_id
    head = {
        "x-up-calling-line-id": "13390905442",
        "x-forwarded-for": "180.99.55.207",
        "x-Called-Station-id": "test",
        "x-User-Location-Info": "test",
        "X-Rat-Type": "test",
        "X_Application_Auth": X_Application_Auth,
        "X-Request-At": date,
        "X-Application-Id": app_id
    }
    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)
    compressedData = eval(response.read().decode())['result']
    print(type(compressedData))
    return compressedData

def check(self,speed_id,date,X_Application_Auth,app_id,security_token):
    url = "http://61.160.149.236:10000/qos-api/speeding?speed_id=" + speed_id
    head = {
        "x-up-calling-line-id": "13390905442",
        "x-forwarded-for": "180.99.55.207",
        "x-Called-Station-id": "test",
        "x-User-Location-Info": "test",
        "X-Rat-Type": "test",
        "X-IMEI":"test",
        "X-Request-At": date,
        "X-Application-Id": app_id,
        "X_Application_Auth": X_Application_Auth,
        "speed_id":speed_id,
        "security_token":security_token,
        "dst_info":"10.1.1.1",

    }









