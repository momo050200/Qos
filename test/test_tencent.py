#coding=utf-8

import unittest
from common.MD5 import MD5
from common.Common import *
from time import sleep

class test_tencent(unittest.TestCase):
    def setUp(self):
        self.file_path = '..\common\cfginfo.ini'
        self.head_get_token = IniReader(self.file_path).get_dict('head_get_token')
        self.X_Application_id = self.head_get_token['X-Application-Id']
        self.date, self.X_Application_Auth = MD5(self.X_Application_id)
        self.x_up_calling_line_id = self.head_get_token['X-Up-Calling-Line-Id']
        self.x_forwarded_for = self.head_get_token['X-Forwarded-For']
        self.head = {
            "X-Request-At": self.date,
            "X-Application-Id": self.X_Application_id,
            "X-Application-Auth": self.X_Application_Auth,
        }

    def tearDown(self):
        pass

    # def test_01_successful(self):
    #     '''成功流程：获取token，申请提速，检查提速，撤销提速，检查提速'''
    #     #step1 获取token
    #     token=get_token(self,self.head_get_token)['result']
    #     print('step1 获取token：'+str(token))
    #     #step2 申请提速
    #     result2 = {'ResultMessage': 'Successful', 'ResultCode': 0}
    #     r=speeding_tencent(self,self.head,token)
    #     print('step2 申请提速:'+str(r))
    #     speed_id=r['CorrelationId']
    #     #step3 检查提速结果
    #     result3 = {'msg':'成功','code':'0'}
    #     c=check(self,speed_id,self.head,results=result3)
    #     print('step3 检查提速结果：'+str(c))
    #     #step4 撤销提速
    #     result4 = {'result':{'Done': True,'speeed_id': speed_id}}
    #     d=delete_speeding(self,speed_id,self.head,req_id='DynamicQoS/',results=result4)
    #     print('step4 撤销提速：'+str(d))
    #     #step5 检查撤销提速结果
    #     result5 = {'msg': '对不起，系统异常', 'code': '10000'}
    #     c2 = check(self, speed_id, self.head, results=result5)
    #     print('step5 检查撤销提速结果：'+str(c2))
    #
    #
    # def test_02_with_deleted_token(self):
    #     '''提速时，使用已撤速的token失效'''
    #     # step1 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step1 获取token：' + str(token))
    #     # step2 申请提速
    #     result2 = {'ResultMessage': 'Successful', 'ResultCode': 0}
    #     r = speeding_tencent(self, self.head, token,results=result2)
    #     print('step2 申请提速:' + str(r))
    #     speed_id = r['CorrelationId']
    #     # step3 检查提速结果
    #     result3 = {'msg': '成功', 'code': '0'}
    #     c = check(self, speed_id, self.head, results=result3)
    #     print('step3 检查提速结果：' + str(c))
    #     # step4 撤销提速
    #     result4 = {'result': {'Done': True, 'speeed_id': speed_id}}
    #     d = delete_speeding(self, speed_id, self.head, results=result4,req_id='DynamicQoS/')
    #     print('step4 撤销提速：' + str(d))
    #     # step5 检查撤销提速结果
    #     result5 = {'msg': '对不起，系统异常', 'code': '10000'}
    #     c2 = check(self, speed_id, self.head, results=result5)
    #     print('step5 检查撤销提速结果：' + str(c2))
    #     # step6 使用失效的token申请提速
    #     result6 = {'code':6254,'message':'认证失败'}
    #     r = speeding(self, self.head, token, results=result6)
    #     print('step6 使用失效的token申请提速:' + str(r))
    #
    # def test_03_with_speed_id_timeout(self):
    #     '''提速后，等待speed_id失效后，使用失效speed_id'''
    #
    #     # step1 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step1 获取token：' + str(token))
    #     # step2 申请提速
    #     result2 = {'ResultMessage': 'Successful', 'ResultCode': 0}
    #     r = speeding_tencent(self, self.head, token,results=result2)
    #     print('step2 申请提速:' + str(r))
    #     speed_id = r['CorrelationId']
    #     # step3 检查提速结果
    #     result3 = {'msg': '成功', 'code': '0'}
    #     c = check(self, speed_id,self.head, results=result3)
    #     print('step3 检查提速结果：' + str(c))
    #     # step4,等待提速时长结束，提速时长默认3分钟，每10s轮巡一次
    #     sleep(190)
    #     print('step4 等待提速时长结束')
    #     # step5 检查撤销提速结果
    #     result5 = {'msg': '对不起，系统异常', 'code': '10000'}
    #     c2 = check(self, speed_id,self.head, results=result5)
    #     print('step5 检查撤销提速结果：' + str(c2))

    # def test_04_token_on_timeout(self):
    #     '''提速时，token失效时间180s，当申请token后179s，申请提速，成功'''
    #     # step1 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step1 获取token：' + str(token))
    #     #等待179s
    #     sleep(179)
    #     # step2 使用未失效的token申请提速
    #     result2 = {'ResultMessage': 'Successful', 'ResultCode': 0}
    #     r = speeding_tencent(self, self.head, token,results=result2)
    #     print('step2 使用濒临失效的token申请提速:' + str(r))

    # def test_05_token_timeout(self):
    #     '''提速时，使用已失效的token'''
    #     # step1 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step1 获取token：' + str(token))
    #     #等待181s
    #     sleep(181)
    #     # step2 使用未失效的token申请提速
    #     result2 = {"ResultCode":254,"ResultMessage":"Auth Failed"}
    #     r = speeding_tencent(self, self.head, token, results=result2)
    #     print('step2 使用失效的token申请提速:' + str(r))

    # def test_06_token_wrong(self):
    #     '''提速时，token错误'''
    #     # step1 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step1 获取token：' + str(token))
    #     # step2 使用错误的token申请提速
    #     wrong_token=token+'123'
    #     result2 = {"ResultCode":254,"ResultMessage":"Auth Failed"}
    #     r = speeding_tencent(self, self.head, wrong_token,results=result2)
    #     print('step2 使用错误的token申请提速:' + str(r))

    def  test_07_dst_info_illegal_1(self):
        '''sp发起，访问提速平台,参数非法DestinationIpAdress='123123',创建提速通道失败'''    #
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info="123123"
        # step2 申请提速
        result2 ={"ResultCode":129,"ResultMessage":"Invalid service information"}
        r = speeding_tencent(self, self.head, token,dst_info_ip=dst_info,results=result2)
        print('step2 DestinationIpAdress="123123"，创建提速失败:' + str(r))

    def  test_07_dst_info_illegal_2(self):
        '''sp发起，访问提速平台,参数SourcePort='abcd',创建提速通道失败'''
        # step1 获取token
        token = get_token(self,self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_port='abcd'
        # step2 申请提速
        result2 ={"ResultCode":129,"ResultMessage":"Invalid service information"}
        r = speeding_tencent(self, self.head, token,dst_port=dst_port,results=result2)
        print('step2 SourcePort="abcd"，提速失败:' + str(r))


    def  test_07_dst_info_illegal_3(self):
        '''sp发起，访问提速平台,参数DestinationIpAdress='10.23.226.',创建提速通道失败'''
        # step1 获取token
        token = get_token(self,self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info = '10.23.226.'
        # step2 申请提速
        result2 ={"ResultCode":129,"ResultMessage":"Invalid service information"}
        r = speeding_tencent(self, self.head, token,dst_info_ip=dst_info,results=result2)
        print('step2 DestinationIpAdress="10.23.226."，创建提速失败:' + str(r))

    def  test_07_dst_info_illegal_4(self):
        '''sp发起，访问提速平台,参数DestinationIpAdress='10.23.22.726.',创建提速通道失败'''
        # step1 获取token
        token = get_token(self,self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info = '10.23.22.726'
        # step2 申请提速
        result2 ={"ResultCode":129,"ResultMessage":"Invalid service information"}
        r = speeding_tencent(self, self.head, token,dst_info_ip=dst_info,results=result2)
        print('step2 DestinationIpAdress="10.23.22.726"，创建提速失败:' + str(r))


    def  test_07_dst_info_illegal_5(self):
        '''sp发起，访问提速平台,参数SourcePort='0',创建提速通道失败'''
        # step1 获取token
        token = get_token(self,self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_port='0'
        # step2 申请提速
        result2 ={"ResultCode":129,"ResultMessage":"Invalid service information"}
        r = speeding_tencent(self, self.head, token,dst_port=dst_port,results=result2)
        print('step2 DestinationPort="abcd"，提速失败:' + str(r))


    def  test_07_dst_info_illegal_6(self):
        '''sp发起，访问提速平台,参数SourcePort='65536',创建提速通道失败'''
        # step1 获取token
        token = get_token(self,self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_port='65536'
        # step2 申请提速
        result2 ={"ResultCode":129,"ResultMessage":"Invalid service information"}
        r = speeding_tencent(self, self.head, token,dst_port=dst_port,results=result2)
        print('step2 DestinationPort="65536"，提速失败:' + str(r))

    # def test_13_turing_success(self):
    #     '''链路轮巡验证：码段对应两个加速通道，动态删除其中一条链路，使用另一条链路加速成功'''    #
    #     # step1 删除链路1
    #     product_key = IniReader(self.file_path).get_value('remove_product','product_key')
    #     product_key = product_key[0]
    #     result1 = {"code":"0","msg":"成功"}
    #     r = remove_product(self,product_key=product_key,results=result1)
    #     print('step1 删除链路：' + product_key)
    #     # step2 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step2 获取token：' + str(token))
    #     # step3 使用剩余的链路申请提速
    #     result3 = {'result': {'Done': 'True'}}
    #     r = speeding_tencent(self, self.head, token, results=result3)
    #     print('step3 使用剩余链路申请提速:' + str(r))
    #     speed_id = r['result']['speeed_id']
    #     # step4 检查提速结果
    #     result4 = {'msg': '成功', 'code': '0'}
    #     c = check(self, speed_id,self.head, result4)
    #     print('step4 检查提速结果：' + str(c))
    #     # step5 重新添加step1中删除的链路
    #     result5 = {"code":"0","msg":"成功"}
    #     a = add_product(self,node_ip_port=product_key,results=result5)
    #     print('step5 重新添加step1中删除的链路：' + str(a))
    #
    #
    # def test_14_remove_link_and_check(self):
    #     '''库里面有3条链路情况下，删除全部链路并校验是否能够提速'''
    #     product_key = IniReader(self.file_path).get_value('remove_product','product_key')
    #     result_remove = {"code": "0", "msg": "成功"}
    #     # 删除全部链路
    #     for i in range(len(product_key)):
    #         link_remove = remove_product(self, product_key[i], result_remove)
    #         print('step' + str(i) + "删除链路：" + str(link_remove))
    #     # MD5加密
    #     # step3 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step3 获取token：' + str(token))
    #     # step4 申请提速
    #     result2 = {'code': 6000, 'message': '暂时不能提速'}
    #     r = speeding_tencent(self, self.head, token, result2)
    #     print('step4 申请提速:' + str(r))
    #     # 重新新增被删除的3条链路
    #     result_add = {'code': '0', 'msg': '成功'}
    #     for i in range(len(product_key)):
    #         link_add = add_product(self, node_ip_port=product_key[i], results=result_add)
    #         print('step' + str(i) + "新增链路：" + str(link_add))
    #     # step6 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step3 获取token：' + str(token))
    #     # step7 申请提速
    #     result2 = {'ResultMessage': 'Successful', 'ResultCode': 0}
    #     r = speeding_tencent(self, self.head, token, result2)
    #     print('step4 申请提速:' + str(r))









if __name__ == "__main__":
    unittest.main()
