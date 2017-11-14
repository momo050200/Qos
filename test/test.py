#coding=utf-8

import unittest
from common_interface import CommonInterface as C
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
        token=get_token(self,X_Application_id,date,X_Application_Auth)
        print(token)
        # print('获取token：'+str(token))
        result2 = {'result':{'Done':'True'}}
        r=speeding(self,X_Application_id,date,X_Application_Auth,token,result2)
        print('申请提速:'+str(r))
        speed_id=r['result']['speeed_id']
        result3 = {'msg':'成功','code':'0'}
        c=check(self,speed_id,X_Application_id,date,X_Application_Auth,result3)
        print('检查提速结果：'+str(c))
        result4 = {}
        d=delete_speeding(self,speed_id,X_Application_id,date,X_Application_Auth,result4)
        print('撤销提速：'+str(d))
        result5 = {'msg': '成功', 'code': '0'}
        c2 = check(self, speed_id, X_Application_id, date, X_Application_Auth, result5)
        print('检查撤销提速结果：'+str(c2))






if __name__ == "__main__":
    unittest.main()
