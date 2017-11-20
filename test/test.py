#coding=utf-8

import unittest
from common.MD5 import MD5
from common.Common import get_token,speeding,check,delete_speeding,remove_product,add_product
from time import sleep

class test(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_01_successful(self):
        '''成功流程：获取token，申请提速，检查提速，撤销提速，检查提速'''
        X_Application_id = '12345678'
        date, X_Application_Auth = MD5(X_Application_id)
        #step1 获取token
        token=get_token(self,X_Application_id,date,X_Application_Auth)['result']
        print('step1 获取token：'+str(token))
        #step2 申请提速
        result2 = {'result': {'Done': 'True'}}
        r=speeding(self,X_Application_id,date,X_Application_Auth,token,result2)
        print('step2 申请提速:'+str(r))
        speed_id=r['result']['speeed_id']
        #step3 检查提速结果
        result3 = {'msg':'成功','code':'0'}
        c=check(self,speed_id,X_Application_id,date,X_Application_Auth,result3)
        print('step3 检查提速结果：'+str(c))
        #step4 撤销提速
        result4 = {'result':{'Done': True,'speeed_id': speed_id}}
        d=delete_speeding(self,speed_id,X_Application_id,date,X_Application_Auth,result4)
        print('step4 撤销提速：'+str(d))
        #step5 检查撤销提速结果
        result5 = {'msg': '对不起，系统异常', 'code': '10000'}
        c2 = check(self, speed_id, X_Application_id, date, X_Application_Auth, result5)
        print('step5 检查撤销提速结果：'+str(c2))

    # def test_02_get_token_faile_with_none_app_id(self):
    #     '''获取token时不传入：X-Application-Id'''
    #     X_Application_id = ''
    #     date,X_Application_Auth = MD5(X_Application_id)
    #     result = {"code":"50000"}
    #     get_token(self,X_Application_id,date,X_Application_Auth,result)

    # def test_03_get_token_faile_with_wrong_app_id(self):
    #     '''获取token时传入：X-Application-Id非法'''
    #     X_Application_id = 'abc#2323434'
    #     date, X_Application_Auth = MD5(X_Application_id)
    #     result = {"code":"50000"}
    #     get_token(self,X_Application_id,date,X_Application_Auth,result)

    # def test_04_get_token_fail_with_app_id_not_in_system(self):
    #     '''获取token时传入：X-Application-Id在系统中不存在'''
    #     X_Application_id = '9876654321'
    #     date, X_Application_Auth = MD5(X_Application_id)
    #     result = {"code":"50000"}
    #     get_token(self,X_Application_id,date,X_Application_Auth,result)

    # def test_05_get_token_faile_with_null_X_Request_At(self):
    #     '''获取token时传入：X-Request-At为空'''
    #     X_Application_id = '12345678'
    #     date,X_Application_Auth = MD5(X_Application_id)
    #     date = ''
    #     result = {"code": "40003"}
    #     get_token(self,X_Application_id,date,X_Application_Auth,result)

    def test_06_with_deleted_token(self):
        '''提速时，使用已撤速的token失效'''
        X_Application_id = '12345678'
        date, X_Application_Auth = MD5(X_Application_id)
        # step1 获取token
        token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
        print('step1 获取token：' + str(token))
        # step2 申请提速
        result2 = {'result': {'Done': 'True'}}
        r = speeding(self, X_Application_id, date, X_Application_Auth, token, result2)
        print('step2 申请提速:' + str(r))
        speed_id = r['result']['speeed_id']
        # step3 检查提速结果
        result3 = {'msg': '成功', 'code': '0'}
        c = check(self, speed_id, X_Application_id, date, X_Application_Auth, result3)
        print('step3 检查提速结果：' + str(c))
        # step4 撤销提速
        result4 = {'result': {'Done': True, 'speeed_id': speed_id}}
        d = delete_speeding(self, speed_id, X_Application_id, date, X_Application_Auth, result4)
        print('step4 撤销提速：' + str(d))
        # step5 检查撤销提速结果
        result5 = {'msg': '对不起，系统异常', 'code': '10000'}
        c2 = check(self, speed_id, X_Application_id, date, X_Application_Auth, result5)
        print('step5 检查撤销提速结果：' + str(c2))
        # step6 使用失效的token申请提速
        result6 = {'code':5065,'message':'资源申请失败'}
        r = speeding(self, X_Application_id, date, X_Application_Auth, token, result6)
        print('step6 使用失效的token申请提速:' + str(r))

    # def test_07_with_speed_id_timeout(self):
    #     '''提速后，等待speed_id失效后，使用失效speed_id'''
    #     X_Application_id = '12345678'
    #     date, X_Application_Auth = MD5(X_Application_id)
    #     # step1 获取token
    #     token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
    #     print('step1 获取token：' + str(token))
    #     # step2 申请提速
    #     result2 = {'result': {'Done': 'True'}}
    #     r = speeding(self, X_Application_id, date, X_Application_Auth, token, result2)
    #     print('step2 申请提速:' + str(r))
    #     speed_id = r['result']['speeed_id']
    #     # step3 检查提速结果
    #     result3 = {'msg': '成功', 'code': '0'}
    #     c = check(self, speed_id, X_Application_id, date, X_Application_Auth, result3)
    #     print('step3 检查提速结果：' + str(c))
    #     # step4,等待提速时长结束，提速时长默认3分钟
    #     sleep(180)
    #     print('step4 等待提速时长结束')
    #     # step5 检查撤销提速结果
    #     result5 = {'msg': '对不起，系统异常', 'code': '10000'}
    #     c2 = check(self, speed_id, X_Application_id, date, X_Application_Auth, result5)
    #     print('step5 检查撤销提速结果：' + str(c2))
    #     # step6 使用失效的token申请提速
    #     result6 = {'code':5065,'message':'资源申请失败'}
    #     r = speeding(self, X_Application_id, date, X_Application_Auth, token, result6)
    #     print('step6 使用失效的token申请提速:' + str(r))

    def test_08_token_on_timeout(self):
        '''提速时，token失效时间180s，当申请token后179s，申请提速，成功'''
        X_Application_id = '12345678'
        date, X_Application_Auth = MD5(X_Application_id)
        # step1 获取token
        token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
        print('step1 获取token：' + str(token))
        #等待179s
        sleep(179)
        # step2 使用未失效的token申请提速
        result2 = {'result': {'Done': 'True'}}
        r = speeding(self, X_Application_id, date, X_Application_Auth, token, result2)
        print('step2 使用濒临失效的token申请提速:' + str(r))

    def test_09_token_timeout(self):
        '''提速时，使用已失效的token'''
        X_Application_id = '12345678'
        date, X_Application_Auth = MD5(X_Application_id)
        # step1 获取token
        token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
        print('step1 获取token：' + str(token))
        #等待181s
        sleep(181)
        # step2 使用未失效的token申请提速
        result2 = {'code':5065,'message':'资源申请失败'}
        r = speeding(self, X_Application_id, date, X_Application_Auth, token, result2)
        print('step2 使用失效的token申请提速:' + str(r))

    def test_10_token_wrong(self):
        '''提速时，token错误'''
        X_Application_id = '12345678'
        date, X_Application_Auth = MD5(X_Application_id)
        # step1 获取token
        token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
        print('step1 获取token：' + str(token))
        # step2 使用错误的token申请提速
        wrong_token=token+'123'
        result2 = {'code':5065,'message':'资源申请失败'}
        r = speeding(self, X_Application_id, date, X_Application_Auth, wrong_token, result2)
        print('step2 使用错误的token申请提速:' + str(r))

    def  test_11_dst_info_illegal(self):
        '''sp发起，访问提速平台,参数非法,创建提速通道失败'''
        X_Application_id = '12345678'
        date, X_Application_Auth = MD5(X_Application_id)
        # step1 获取token
        token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
        print('step1 获取token：' + str(token))
        dst_info='123123'
        # step2 申请提速
        result2 ={'code':5065,'message':'资源申请失败'}
        r = speeding(self, X_Application_id, date, X_Application_Auth, token,dst_info=dst_info,results=result2)
        print('step2 dst_info参数非法，创建提速失败:' + str(r))

    # def  test_12_dst_info_not_exist(self):
    #     '''sp发起，访问提速平台,参数合法但在系统中不存在,创建提速通道失败'''
    #     X_Application_id = '12345678'
    #     date, X_Application_Auth = MD5(X_Application_id)
    #     # step1 获取token
    #     token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
    #     print('step1 获取token：' + str(token))
    #     dst_info='10.1.7.9:2'
    #     # step2 申请提速
    #     result2 ={'code':5065,'message':'资源申请失败'}
    #     r = speeding(self, X_Application_id, date, X_Application_Auth, token,dst_info=dst_info,results=result2)
    #     print('step2 dst_info合法但系统不存在，提速失败:' + str(r))


    def test_13_turing_success(self):
        '''链路轮巡验证：码段对应两个加速通道，动态删除其中一条链路，使用另一条链路加速成功'''
        X_Application_id = '12345678'
        date, X_Application_Auth = MD5(X_Application_id)
        # step1 删除链路1
        product_key = "192.168.203.65:10002"
        result1 = {"code":"0","msg":"成功"}
        r = remove_product(self,product_key=product_key,results=result1)
        print('step1 删除链路：' + product_key)
        # step2 获取token
        token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
        print('step2 获取token：' + str(token))
        # step3 使用剩余的链路申请提速
        result3 = {'result': {'Done': 'True'}}
        r = speeding(self, X_Application_id, date, X_Application_Auth, token, results=result3)
        print('step3 使用剩余链路申请提速:' + str(r))
        speed_id = r['result']['speeed_id']
        # step4 检查提速结果
        result4 = {'msg': '成功', 'code': '0'}
        c = check(self, speed_id, X_Application_id, date, X_Application_Auth, result4)
        print('step4 检查提速结果：' + str(c))
        # step5 重新添加step1中删除的链路
        result5 = {"code":"0","msg":"成功","body":{"key":"192.168.203.65:10002"},"head":{}}
        a = add_product(self,results=result5)
        print('step5 重新添加step1中删除的链路：' + str(a))


    def test_14_remove_link_and_check(self):
        '''库里面有3条链路情况下，删除全部链路并校验是否能够提速'''
        product_key = ['192.168.203.65:3868', '192.168.203.65:10001', '192.168.203.65:10002']
        result_remove = {"code": "0", "msg": "成功"}
        # 删除全部链路
        for i in range(len(product_key)):
            link_remove = remove_product(self, product_key[i], result_remove)
            print('step' + str(i) + "删除链路：" + str(link_remove))
        # MD5加密
        X_Application_id = '12345678'
        date, X_Application_Auth = MD5(X_Application_id)
        # step3 获取token
        token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
        print('step3 获取token：' + str(token))
        # step4 申请提速
        result2 = {'code': 5065, 'message': '资源申请失败'}
        r = speeding(self, X_Application_id, date, X_Application_Auth, token, result2)
        print('step4 申请提速:' + str(r))
        # 重新新增被删除的3条链路
        result_add = {'code': '0', 'msg': '成功'}
        for i in range(len(product_key)):
            link_add = add_product(self, node_ip_port=product_key[i], results=result_add)
            print('step' + str(i) + "新增链路：" + str(link_add))

    def test_15_add_with_wrong_node_ip_port(self):
        '''动态新增时，传入的node_ip_port错误'''
        node_ip_port = '192.168.203.1:10002'
        result = {"code":"10000","msg":"对不起，系统异常"}
        a = add_product(self,node_ip_port=node_ip_port,results=result)
        print('使用错误的node_ip_port动态新增链路：'+ str(a))

    def test_16_add_with_wrong_remote_ip_port(self):
        '''动态新增时，传入的remote_ip_port错误'''
        remote_ip_port = '192.168.203.1:10002'
        result = {"code":"10000","msg":"对不起，系统异常"}
        a = add_product(self,remote_ip_port=remote_ip_port,results=result)
        print('使用错误的remote_ip_port动态新增链路：'+ str(a))

    def test_17_add_with_wrong_remote_hostname(self):
        '''动态新增时，传入的remote_hostname错误'''
        remote_hostname = 'abc'
        result = {"code":"10000","msg":"对不起，系统异常"}
        a = add_product(self,remote_hostname=remote_hostname,results=result)
        print('使用错误的remote_hostname动态新增链路：'+ str(a))

    def test_18_add_with_notmatch_remote_hostname_and_remote_ip_port(self):
        '''动态新增时，传入的remote_hostname与remote_ip_port不匹配'''
        remote_hostname = 'abc'
        remote_ip_port = '192.168.203.1:10002'
        result = {"code":"10000","msg":"对不起，系统异常"}
        a = add_product(self,remote_hostname=remote_hostname,remote_ip_port=remote_ip_port,results=result)
        print('使用不匹配的remote_hostname与remote_ip_port动态新增链路：'+ str(a))




if __name__ == "__main__":
    unittest.main()
