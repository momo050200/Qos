#coding=utf-8

from common_interface import CommonInterface as C
import json,unittest
from IniReader import IniReader

'''
    参数说明：
    X_Application_id：app_id
    date：X-Request-At
    X-Application-Auth：X_Application_Auth
    
'''


def get_token(self, head, results=None):
    global file_path, base_url
    file_path = '..\common\cfginfo.ini'
    base_url = IniReader(file_path).get_value('url', 'base_url')
    get_token = IniReader(file_path).get_value('url', 'get_token')
    url = base_url + get_token
    result = C.get(self, url, data=None, headers=head, results=results)
    return result


def check(self, speed_id, head, results=None):
    check = IniReader(file_path).get_value('url', 'check')
    url = base_url + check + speed_id
    result = C.get(self, url, headers=head, results=results)
    return result


def speeding(self, head, security_token, dst_info=None, results=None, ):
    speeding_xunyou = IniReader(file_path).get_value('url', 'speeding_xunyou')
    url = base_url + speeding_xunyou
    body = eval(IniReader(file_path).get_value('speeding_xunyou_body', 'body'))
    body["security_token"] = security_token
    if dst_info != None:
        body["dst_info"] = dst_info
    result = C.post(self, url, data=body, headers=head, results=results)
    return result


def speeding_tencent(self, head, security_token, results=None, dst_info_ip=None, dst_port=None):
    speeding_tencent = IniReader(file_path).get_value('url', 'speeding_tencent')
    url = base_url + speeding_tencent
    body = eval(IniReader(file_path).get_value('speeding_tencent_body', 'body'))
    body["security_token"] = security_token
    if dst_info_ip != None:
        body["ResourceFeatureProperties"]["FlowProperties"]["DestinationIpAdress"] = dst_info_ip
    if dst_port != None:
        body["ResourceFeatureProperties"]["FlowProperties"]["SourcePort"] = dst_port
    body = json.dumps(body)
    result = C.post(self, url, data=body, headers=head, results=results)
    return result


def delete_speeding(self, speed_id, head, results=None):
    delete_speeding = IniReader(file_path).get_value('url', 'delete_speeding')
    url = base_url + delete_speeding + speed_id
    result = C.delete(self, url, headers=head, results=results)
    return result


def add_product(self, results=None, node_ip_port=None, remote_ip_port=None, remote_hostname=None):
    add_product = IniReader(file_path).get_value('url', 'add_product')
    url = base_url + add_product
    body = eval(IniReader(file_path).get_value('add_product_body', 'body'))
    if node_ip_port != None:
        body["node_ip_port"] = node_ip_port
    if remote_ip_port != None:
        body["remote_ip_port"] = remote_ip_port
    if remote_hostname != None:
        body["remote_hostname"] = remote_hostname
    result = C.post(self, url, data=body, results=results)
    return result


def remove_product(self, product_key, results=None):
    remove_product = IniReader(file_path).get_value('url', 'remove_product')
    url = base_url + remove_product
    body = {
        'key': product_key,
    }
    result = C.post(self, url, data=body, results=results)
    return result




















