#coding=utf-8

import unittest
from common.MD5 import MD5
from common.Common import get_token,speeding,check,delete_speeding

class test(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_successful(self):
        '''成功流程：获取token，申请提速，检查提速，撤销提速，检查提速'''
        X_Application_id = '12345678'
        date, X_Application_Auth = MD5(X_Application_id)
        #step1 获取token
        token=get_token(self,X_Application_id,date,X_Application_Auth)['result']
        print('step1 获取token：'+str(token))
        #step2 申请提速
        result2 = {'result':{'Done':'True'}}
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

    def test_get_token_faile_with_none_app_id(self):
        '''获取token时不传入：X-Application-Id'''
        X_Application_id = ''
        date,X_Application_Auth = MD5(X_Application_id)
        result = {"code":"50000"}
        get_token(self,X_Application_id,date,X_Application_Auth,result)

    def test_get_token_faile_with_wrong_app_id(self):
        '''获取token时传入：X-Application-Id非法'''
        X_Application_id = 'abc#2323434'
        date, X_Application_Auth = MD5(X_Application_id)
        result = {"code":"50000"}
        get_token(self,X_Application_id,date,X_Application_Auth,result)

    def test_get_token_faile_with_app_id_not_in_system(self):
        '''获取token时传入：X-Application-Id在系统中不存在'''
        X_Application_id = '9876654321'
        date, X_Application_Auth = MD5(X_Application_id)
        result = {"code":"50000"}
        get_token(self,X_Application_id,date,X_Application_Auth,result)

    def test_get_token_faile_with_null_X_Request_At(self):
        '''获取token时传入：X-Request-At为空'''
        X_Application_id = '12345678'
        date,X_Application_Auth = MD5(X_Application_id)
        date = ''
        result = {"code": "40003"}
        get_token(self,X_Application_id,date,X_Application_Auth,result)

    def test_token_timeout(self):
        '''提速时，token失效'''
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

    def test_token_wrong(self):
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

    def  test_dst_info_illegal(self):
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

    # def  test_dst_info_not_exist(self):
    #     '''sp发起，访问提速平台,参数合法但在系统中不存在,创建提速通道失败'''
    #     X_Application_id = '12345678'
    #     date, X_Application_Auth = MD5(X_Application_id)
    #     # step1 获取token
    #     token = get_token(self, X_Application_id, date, X_Application_Auth)['result']
    #     print('step1 获取token：' + str(token))
    #     dst_info='10.1.7.9:2'
    #     # step2 申请提速
    #     # result2 ={'code':5065,'message':'资源申请失败'}
    #     r = speeding(self, X_Application_id, date, X_Application_Auth, token,dst_info=dst_info)
    #     print('step2 dst_info合法但系统不存在，提速失败:' + str(r))



if __name__ == "__main__":
    unittest.main()
