#coding=utf-8

import unittest
from common_interface import CommonInterface as C
from common.MD5 import MD5
from common.Common import get_token,speeding,check

class test(unittest.TestCase):
    def setUp(self):
        # self.url = "http://61.160.149.236:10000/qos-api/"
        self.X_Application_id,self.date,self.X_Application_Auth = MD5()

    def tearDown(self):
        pass

    def test_1(self):
        token=get_token(self,self.X_Application_id,self.date,self.X_Application_Auth)['result']
        print(token)
        r=speeding(self,self.X_Application_id,self.date,self.X_Application_Auth,token)
        print(r)
        speed_id=r['result']['speeed_id']
        print(speed_id)
        print(check(self,speed_id,self.X_Application_id,self.date,self.X_Application_Auth))




if __name__ == "__main__":
    unittest.main()
