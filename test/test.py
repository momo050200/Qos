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
        date, X_Application_Auth = MD5(X_Application_id)
        result = {"code":"50000"}
        get_token(self,X_Application_id,date,X_Application_Auth,result)








if __name__ == "__main__":
    unittest.main()
