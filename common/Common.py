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
        body = IniReader(self.file_path).get_value('speeding_xunyou_body', 'body')
        body["security_token"] = security_token
        if dst_info != None:
            body["dst_info"]=dst_info
        result = C.post(self,url,data=body,headers=head,results=results)
        return result

    def speeding_tencent(self,head,security_token,results=None,dst_info_ip=None,dst_port=None):
        url = self.base_url + self.speeding_tencent
        body = IniReader(self.file_path).get_value('speeding_tencent_body', 'body')
        body["security_token"]=security_token
        if dst_info_ip != None:
            body["ResourceFeatureProperties"]["FlowProperties"]["DestinationIpAdress"]=dst_info_ip
        if dst_port != None:
            body["ResourceFeatureProperties"]["FlowProperties"]["SourcePort"]=dst_port
        body = json.dumps(body)
        result = C.post(self,url,data=body,headers=head,results=results)
        return result

    def delete_speeding(self,speed_id,head,results=None):
        url = self.base_url + self.delete_speeding + speed_id
        result = C.delete(self,url,headers=head,results=results)
        return result

    def add_product(self,results=None,node_ip_port=None,remote_ip_port=None,remote_hostname=None):
        url = self.base_url + self.add_product
        body = IniReader(self.file_path).get_value('add_product_body', 'body')
        if node_ip_port!=None:
            body["node_ip_port"]=node_ip_port
        if remote_ip_port!=None:
            body["remote_ip_port"]=remote_ip_port
        if remote_hostname!=None:
            body["remote_hostname"]=remote_hostname
        result = C.post(self,url,data=body,results=results)
        return result

    def remove_product(self,product_key,results=None):
        url = self.base_url + self.remove_product
        body = {
            'key':product_key,
        }
        result = C.post(self,url,data=body,results=results)
        return result











