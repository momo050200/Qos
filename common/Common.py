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
        # "x-up-calling-line-id": "17798502661",
        # "x-forwarded-for": "10.129.201.176",
        "x-up-calling-line-id": "13390905442",
        "x-forwarded-for": "49.95.221.158",
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
    url = "http://61.160.149.236:10000/qos-api/speeding?speeed_id=aar_" + speed_id
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

def add_product(self,results=None,
                node_ip_port='192.168.203.65:10002',
                remote_ip_port='132.224.255.41:13868',
                remote_hostname='pcrf009-b-ot.nj.js.node.epc.mnc011.mcc460.3gppnetwork.org'):
    url = "http://61.160.149.236:10000/qos-api/addProduct"
    body = {
        'id':'101',
        'location_code':'0',
        'service_url':'http://192.168.203.65:18084/qos-bizcore',
        'core_network_company':'0',
        'load_type':'1',
        'networking_type':'0',
        'node_ip_port':node_ip_port,
        'node_hostname':'com.jshx.qos',
        'remote_ip_port':remote_ip_port,
        'remote_hostname':remote_hostname,
        'province_code':'js',
        'delete_flag':'0',
    }
    result = C.post(self,url,data=body,results=results)
    return result

def remove_product(self,product_key,results=None):
    url = "http://61.160.149.236:10000/qos-api/removeProduct"
    body = {
        'key':product_key,
    }
    result = C.post(self,url,data=body,results=results)
    return result











