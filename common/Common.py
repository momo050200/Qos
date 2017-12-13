#coding=utf-8

from common_interface import CommonInterface as C
import json
from IniReader import IniReader



'''
    参数说明：
    X_Application_id：app_id
    date：X-Request-At
    X-Application-Auth：X_Application_Auth
    
'''
class common:
    def __init__(self):
        self.file_path = '.\cfginfo.ini'
        self.base_url = IniReader(self.file_path).get_value('url', 'base_url')
        self.get_token=IniReader(self.file_path).get_value('url', 'get_token')
        self.speeding_xunyou=IniReader(self.file_path).get_value('url', 'speeding_xunyou')
        self.speeding_tencent=IniReader(self.file_path).get_value('url', 'speeding_tencent')
        self.check=IniReader(self.file_path).get_value('url', 'check')
        self.delete_speeding=IniReader(self.file_path).get_value('url', 'delete_speeding')
        self.add_product=IniReader(self.file_path).get_value('url', 'add_product')
        self.remove_product=IniReader(self.file_path).get_value('url', 'remove_product')
        self.speeding_xunyou_body = IniReader(self.file_path).get_dict('speeding_xunyou_body')
        self.dst_info=IniReader(self.file_path).get_value('speeding_xunyou', 'dst_info')


    def get_token(self,head,results=None):
        url = self.base_url+self.get_token
        result = C.get(self,url,data=None,headers=head,results=results)
        return result

    def check(self,speed_id,head,results=None):
        url = self.base_url + self.check+ speed_id
        result = C.get(self,url,headers=head,results=results)
        return result

    def speeding(self,head,security_token,dst_info=None,results=None,):
        url = self.base_url + self.speeding_xunyou
        if dst_info == None:
            dst_info=self.dst_info
        body = {
            "security_token":security_token,
            "dst_info":dst_info,
        }
        body = dict(self.speeding_xunyou_body,**body)
        result = C.post(self,url,data=body,headers=head,results=results)
        return result

    def speeding_tencent(self,head,security_token,results=None,dst_info_ip="60.174.237.91",dst_port=2220,req_id='DynamicQoS'):
        url = self.base_url + req_id
        body = {
            "security_token":security_token,
            "productid":"12345678",
            "userid":"376434384",
            "UserIdentifier":{
                "PublicIP":"x.x.x.x",
                "IP":"x.x.x.x",
                "IMSI":"460030123456789",
                "MSISDN":"+8613810005678"
            },
            "APN":"APNtest",
            "ServiceId":"BufferedStreamingVideo",
            "CPSPID":"SPtest",
            "ResourceFeatureProperties":[
                {
                    "Type":1,
                    "Priority":1,
                    "FlowProperties":[
                        {
                            "Direction":2,
                            "SourceIpAdress":"x.x.x.x",
                            "DestinationIpAdress":dst_info_ip,
                            "SourcePort":dst_port,
                            "DestinationPort":"",
                            "Protocol":"UDP",
                            "MaximumUpStreamSpeedRate":1000000,
                            "MaximumDownStreamSpeedRate":4000000
                        }
                    ],
                    "MinimumUpStreamSpeedRate":200000,
                    "MinimumDownStreamSpeedRate":400000
                }
            ],
            "Duration":600,
            "CallBackURL":"http://XXXXXXXXXXXXXXXXXXX"
        }
        body = json.dumps(body)
        result = C.post(self,url,data=body,headers=head,results=results)
        return result

    def delete_speeding(self,speed_id,head,results=None,req_id='speeding?speeed_id='):
        url = base_url + req_id + speed_id
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











