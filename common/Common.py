#coding=utf-8

from common_interface import CommonInterface as C
from common.MD5 import MD5


def get_token(self, app_id):
    date, X_Application_Auth = MD5()
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
    result = C.get(self, url, data=head)
    return result





