#coding=utf-8

import unittest
from common.MD5 import MD5
from common.Common import *
from time import sleep
from IniReader import IniReader

class test(unittest.TestCase):
    def setUp(self):
        self.file_path = '.\common\cfginfo.ini'
        self.head_get_token = IniReader(self.file_path).get_dict('head_get_token')
        self.X_Application_id = self.head_get_token['X-Application-Id']
        self.date, self.X_Application_Auth = MD5(self.X_Application_id)
        self.x_up_calling_line_id=self.head_get_token['X-Up-Calling-Line-Id']
        self.x_forwarded_for=self.head_get_token['X-Forwarded-For']
        self.head = {
            "X-Request-At": self.date,
            "X-Application-Id": self.X_Application_id,
            "X-Application-Auth": self.X_Application_Auth,
        }


    def tearDown(self):
        pass

    '''
        正常流程测试用例
        test_01：成功流程
    '''
    def test_01_successful(self):
        '''成功流程：获取token，申请提速，检查提速，撤销提速，检查提速'''
        #step1 获取token
        token=get_token(self,self.head_get_token)['result']
        print('step1 获取token：'+str(token))
        #step2 申请提速
        result2 = {'result': {'Done': 'True'}}
        r=speeding(self,self.head,token,results=result2)
        print('step2 申请提速:'+str(r))
        speed_id=r['result']['speeed_id']
        #step3 检查提速结果
        result3 = {'msg':'成功','code':'0'}
        c=check(self,speed_id,self.head,results=result3)
        print('step3 检查提速结果：'+str(c))
        #step4 撤销提速
        result4 = {'result':{'Done': True,'speeed_id': speed_id}}
        d=delete_speeding(self,speed_id,self.head,results=result4)
        print('step4 撤销提速：'+str(d))
        #step5 检查撤销提速结果
        result5 = {'msg': '对不起，系统异常', 'code': '10000'}
        c2 = check(self, speed_id, self.head, results=result5)
        print('step5 检查撤销提速结果：'+str(c2))


    '''
        获取token失败测试用例

        test_02：appid
        test_03：X-Up-Calling-Line-Id
        test_04：x-forwared-for
        test_05：x-imsi-id
        test_06：X_Application_Id
        test_07：X_Request_At

    '''
    def test_02_01_with_none_app_id(self):
        '''获取token，app_id不传'''
        req_id = 't1?'
        # step1 获取token,传入app_id为空
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, self.head_get_token, req_id=req_id, results=result)

    def test_02_02_with_null_appid(self):
        '''获取token，app_id为空'''
        req_id = 't1?appid='
        # step1 获取token,传入app_id为空
        result = {'error': {'code': '4002', 'message': 'Not supported!'}}
        get_token(self, self.head_get_token, req_id=req_id, results=result)

    def test_02_03_with_wrong_app_id(self):
        '''获取token,app_id错误'''
        req_id = 't1?appid=abc'
        # step1 获取token,传入app_id为空
        result = {'error': {'code': '4002', 'message': 'Not supported!'}}
        get_token(self, self.head_get_token, req_id=req_id, results=result)

    def test_03_01_with_none_x_up_calling_line_id(self):
        '''获取token，X-Up-Calling-Line-Id不传'''
        del self.head_get_token['X-Up-Calling-Line-Id']
        head = self.head_get_token
        # step1 获取token,X-Up-Calling-Line-Id不传
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, head,results=result)

    def test_03_02_with_null_x_up_calling_line_id(self):
        '''获取token，X-Up-Calling-Line-Id为空'''
        self.head_get_token['X-Up-Calling-Line-Id']=""
        head = self.head_get_token
        # step1 获取token,X-Up-Calling-Line-Id不传
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, head,results=result)

    def test_03_03_with_wrong_x_up_calling_line_id(self):
        '''获取token，X-Up-Calling-Line-Id格式错误'''
        self.head_get_token['X-Up-Calling-Line-Id']="189123"
        head = self.head_get_token
        # step1 获取token,X-Up-Calling-Line-Id格式错误
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, head,results=result)

    def test_03_04_with_not_support_x_up_calling_line_id(self):
        '''获取token，X-Up-Calling-Line-Id所在省份不支持'''
        self.head_get_token['X-Up-Calling-Line-Id'] = "13357131223"
        head = self.head_get_token
        # step1 获取token,X-Up-Calling-Line-Id所在省份不支持
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        # get_token(self, head, results=result)
        print(get_token(self, head, ))

    def test_03_05_with_not_support_x_up_calling_line_id(self):
        '''获取token，X-Up-Calling-Line-Id格式错误'''
        self.head_get_token['X-Up-Calling-Line-Id'] = "17397952473a"
        head = self.head_get_token
        # step1 获取token,X-Up-Calling-Line-Id格式错误
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, head, results=result)

    def test_04_01_with_none_x_forwared_for(self):
        '''获取token，x-forwared-for不传'''
        del self.head_get_token['X-Forwarded-For']
        head = self.head_get_token
        # step1 获取token,x-forwared-for不传
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, head, results=result)

    def test_04_02_with_null_x_forwared_for(self):
        '''获取token，x-forwared-for为空'''
        self.head_get_token['X-Forwarded-For'] = ""
        head = self.head_get_token
        # step1 获取token,x-forwared-for为空
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, head, results=result)

    def test_04_03_with_wrong_x_forwared_for(self):
        '''获取token，x-forwared-for=10.252.20.645'''
        self.head_get_token['X-Forwarded-For'] = "10.252.20.645"
        head = self.head_get_token
        # step1 获取token,x-forwared-for=10.252.20.645
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, head, results=result)

    def test_04_04_with_wrong_x_forwared_for(self):
        '''获取token，x-forwared-for=10.252.64'''
        self.head_get_token['X-Forwarded-For'] = "10.252.64"
        head = self.head_get_token
        # step1 获取token,x-forwared-for=10.252.64
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, head, results=result)

    def test_05_01_with_none_X_IMSI_Id(self):
        '''获取token，X-IMSI-Id不传'''
        del self.head_get_token['X-IMSI-Id']
        head = self.head_get_token
        # step1 获取token,X-IMSI-Id不传
        result = {'error': {'code': '4003', 'message': 'Access Denied!'}}
        get_token(self, head, results=result)

    def test_05_02_with_null_X_IMSI_Id(self):
        '''获取token，X-IMSI-Id为空'''
        self.head_get_token['X-IMSI-Id']=''
        head = self.head_get_token
        # step1 获取token,X-IMSI-Id为空
        result = {'error': {'message': 'Access Denied!', 'code': '4003'}}
        get_token(self, head, results=result)
        # print(get_token(self, head, ))

    def test_05_03_with_wrong_X_IMSI_Id(self):
        '''获取token，X-IMSI-Id错误'''
        self.head_get_token['X-IMSI-Id'] = "abcdefg+@#$"
        head = self.head_get_token
        print(head)
        # step1 获取token,X-IMSI-Id错误
        result = {'error': {'message': 'Access Denied!', 'code': '4003'}}
        get_token(self, head, results=result)

    def test_05_04_with_wrong_X_IMSI_Id(self):
        '''获取token，X-IMSI-Id格式错误（超过11位）'''
        self.head_get_token['X-IMSI-Id'] = "4601102175011115"
        head = self.head_get_token
        print(head)
        # step1 获取token,X-IMSI-Id错误
        result = {'error': {'message': 'Access Denied!', 'code': '4003'}}
        get_token(self, head, results=result)

    # def test_06_01_with_none_X_Application_Id(self):
    #     '''获取token时不传入：X-Application-Id'''
    #     X_Application_id = ''
    #     date,X_Application_Auth = MD5(X_Application_id)
    #     self.head_get_token['X-Request-At'] = date
    #     self.head_get_token['X-Application-Auth'] = X_Application_Auth
    #     self.head_get_token['X-Application-Id'] = X_Application_id
    #     head = self.head_get_token
    #     result = {"code":"50000"}
    #     get_token(self,head,results=result)

    # def test_06_02_with_wrong_X_Application_Id(self):
    #     '''获取token时传入：X-Application-Id非法'''
    #     X_Application_id = 'abc#2323434'
    #     date, X_Application_Auth = MD5(X_Application_id)
    #     self.head_get_token['X-Request-At'] = date
    #     self.head_get_token['X-Application-Auth'] = X_Application_Auth
    #     self.head_get_token['X-Application-Id'] = X_Application_id
    #     head = self.head_get_token
    #     result = {"code": "50000"}
    #     get_token(self, head, results=result)
    #
    # def test_06_03_with_X_Application_Id_not_in_system(self):
    #     '''获取token时传入：X-Application-Id在系统中不存在'''
    #     X_Application_id = '9876654321'
    #     date, X_Application_Auth = MD5(X_Application_id)
    #     self.head_get_token['X-Request-At'] = date
    #     self.head_get_token['X-Application-Auth'] = X_Application_Auth
    #     self.head_get_token['X-Application-Id'] = X_Application_id
    #     head = self.head_get_token
    #     result = {"code": "50000"}
    #     get_token(self, head, results=result)
    #
    # def test_07_01_with_null_X_Request_At(self):
    #     '''获取token时传入：X-Request-At为空'''
    #     date = ''
    #     self.head_get_token['X-Request-At'] = date
    #     head = self.head_get_token
    #     result = {"code": "40003"}
    #     get_token(self,head,result)


    '''
        加速失败测试用例

        test_08：sercurity_token
        test_09：speed_id到期自动拆速成功
        test_10：dst_info

    '''
    def test_08_01_with_deleted_token(self):
        '''提速时，使用已撤速的token失效'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        # step2 申请提速
        result2 = {'result': {'Done': 'True'}}
        r = speeding(self, self.head, security_token=token, results=result2)
        print('step2 申请提速:' + str(r))
        speed_id = r['result']['speeed_id']
        # step3 检查提速结果
        result3 = {'msg': '成功', 'code': '0'}
        c = check(self, speed_id, self.head, results=result3)
        print('step3 检查提速结果：' + str(c))
        # step4 撤销提速
        result4 = {'result': {'Done': True, 'speeed_id': speed_id}}
        d = delete_speeding(self, speed_id, self.head, results=result4)
        print('step4 撤销提速：' + str(d))
        # step5 检查撤销提速结果
        result5 = {'msg': '对不起，系统异常', 'code': '10000'}
        c2 = check(self, speed_id, self.head, results=result5)
        print('step5 检查撤销提速结果：' + str(c2))
        # step6 使用失效的token申请提速
        result6 = {'code':6254,'message':'认证失败'}
        r = speeding(self, self.head, token, results=result6)
        print('step6 使用失效的token申请提速:' + str(r))

    def test_08_02_token_on_timeout(self):
        '''提速时，token失效时间180s，当申请token后179s，申请提速，成功'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        #等待179s
        sleep(179)
        # step2 使用未失效的token申请提速
        result2 = {'result': {'Done': 'True'}}
        r = speeding(self, self.head, token, results=result2)
        print('step2 使用濒临失效的token申请提速:' + str(r))

    def test_08_03_token_timeout(self):
        '''提速时，使用已失效的token'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        #等待181s
        sleep(181)
        # step2 使用未失效的token申请提速
        result2 = {'code':6254,'message':'认证失败'}
        r = speeding(self, self.head, token, results=result2)
        print('step2 使用失效的token申请提速:' + str(r))

    def test_08_04_token_wrong(self):
        '''提速时，token错误'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        # step2 使用错误的token申请提速
        wrong_token=token+'123'
        result2 = {'code':6254,'message':'认证失败'}
        r = speeding(self, self.head, wrong_token, results=result2)
        print('step2 使用错误的token申请提速:' + str(r))

    def test_09_with_speed_id_timeout(self):
        '''提速后，等待speed_id失效后，使用失效speed_id'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        # step2 申请提速
        result2 = {'result': {'Done': 'True'}}
        r = speeding(self, self.head, token, results=result2)
        print('step2 申请提速:' + str(r))
        speed_id = r['result']['speeed_id']
        # step3 检查提速结果
        result3 = {'msg': '成功', 'code': '0'}
        c = check(self, speed_id,self.head, results=result3)
        print('step3 检查提速结果：' + str(c))
        # step4,等待提速时长结束，提速时长默认3分钟，每10s轮巡一次
        sleep(190)
        print('step4 等待提速时长结束')
        # step5 检查撤销提速结果
        result5 = {'msg': '对不起，系统异常', 'code': '10000'}
        c2 = check(self, speed_id,self.head, results=result5)
        print('step5 检查撤销提速结果：' + str(c2))

    def  test_10_01_dst_info_illegal(self):
        '''sp发起，访问提速平台,dst_info格式非法,dst_info='123123',创建提速通道失败'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info='123123'
        # step2 申请提速
        result2 ={'code':6253,'message':'参数不合法'}
        r = speeding(self, self.head, token,dst_info=dst_info,results=result2)
        print('step2 dst_info参数非法，创建提速失败:' + str(r))

    def  test_10_02_dst_info_illegal(self):
        '''sp发起，访问提速平台,dst_info格式非法,dst_info='10.1.1.335:155'创建提速通道失败'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info='10.1.1.335:155'
        # step2 申请提速
        result2 ={'code':6253,'message':'参数不合法'}
        r = speeding(self, self.head, token,dst_info=dst_info,results=result2)
        print('step2 dst_info参数非法，创建提速失败:' + str(r))

    def  test_10_03_dst_info_illegal(self):
        '''sp发起，访问提速平台,dst_info格式非法,dst_info='10.1.1.5:'创建提速通道失败'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info='10.1.1.5:'
        # step2 申请提速
        result2 ={'code':6253,'message':'参数不合法'}
        r = speeding(self, self.head, token,dst_info=dst_info,results=result2)
        print('step2 dst_info参数非法，创建提速失败:' + str(r))

    def  test_10_04_dst_info_with_no_port(self):
        '''sp发起，访问提速平台,dst_info格式正确,dst_info='10.1.1.5'创建提速通道成功'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info='10.1.1.5'
        # step2 申请提速
        result2 ={'result': {'Done': 'True'}}
        r = speeding(self, self.head, token,dst_info=dst_info,results=result2)
        print('step2 dst_info参数正确，创建提速成功:' + str(r))

    def  test_10_05_dst_info_illegal(self):
        '''sp发起，访问提速平台,dst_info格式非法,dst_info='10.1.1:155'创建提速通道失败'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info = '10.1.1:155'
        # step2 申请提速
        result2 = {'code': 6253, 'message': '参数不合法'}
        r = speeding(self, self.head, token, dst_info=dst_info, results=result2)
        print('step2 dst_info参数非法，创建提速失败:' + str(r))

    def  test_10_06_dst_info_illegal(self):
        '''sp发起，访问提速平台,dst_info格式非法,dst_info='60.174.237.91:0'创建提速通道失败'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info = '60.174.237.91:0'
        # step2 申请提速
        result2 = {'code': 6253, 'message': '参数不合法'}
        r = speeding(self, self.head, token, dst_info=dst_info, results=result2)
        print('step2 dst_info参数非法，创建提速失败:' + str(r))

    def  test_10_07_dst_info_illegal(self):
        '''sp发起，访问提速平台,dst_info格式非法,dst_info='60.174.237.91:65536'创建提速通道失败'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info = '60.174.237.91:65536'
        # step2 申请提速
        result2 = {'code': 6253, 'message': '参数不合法'}
        r = speeding(self, self.head, token, dst_info=dst_info, results=result2)
        print('step2 dst_info参数非法，创建提速失败:' + str(r))

    def  test_10_08_dst_info_illegal(self):
        '''sp发起，访问提速平台,dst_info格式非法,dst_info='60.174.237.91:abc'创建提速通道失败'''
        # step1 获取token
        token = get_token(self, self.head_get_token)['result']
        print('step1 获取token：' + str(token))
        dst_info = '60.174.237.91:abc'
        # step2 申请提速
        result2 = {'code': 6253, 'message': '参数不合法'}
        r = speeding(self, self.head, token, dst_info=dst_info, results=result2)
        print('step2 dst_info参数非法，创建提速失败:' + str(r))


    '''
        动态新增、删除测试用例

    '''

    # def test_11_turing_success(self):
    #     '''链路轮巡验证：码段对应两个加速通道，动态删除其中一条链路，使用另一条链路加速成功'''
    #     # step1 删除链路1
    #     product_key = (IniReader(self.file_path).get_value('remove_product', 'product_key'))[0]
    #     result1 = {"code":"0","msg":"成功"}
    #     r = remove_product(self,product_key=product_key,results=result1)
    #     print('step1 删除链路：' + product_key)
    #     # step2 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step2 获取token：' + str(token))
    #     # step3 使用剩余的链路申请提速
    #     result3 = {'result': {'Done': 'True'}}
    #     r = speeding(self, self.head, token, results=result3)
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
    # def test_12_remove_link_and_check(self):
    #     '''库里面有3条链路情况下，删除全部链路并校验是否能够提速'''
    #     product_key = IniReader(self.file_path).get_value('remove_product', 'product_key')
    #     result_remove = {"code": "0", "msg": "成功"}
    #     # step1 删除全部链路
    #     print('step1' + "删除链路：")
    #     for i in range(len(product_key)):
    #         link_remove = remove_product(self, product_key[i], result_remove)
    #         print("删除链路" + product_key[i] + ":" + str(link_remove))
    #     # step2 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step2 获取token：' + str(token))
    #     # step3 申请提速
    #     result2 = {'code': 6000, 'message': '暂时不能提速'}
    #     r = speeding(self, self.head, token, )
    #     print('step3 申请提速:' + str(r))
    #     # step4 重新新增被删除的3条链路
    #     print('step4 新增链路：')
    #     result_add = {'code': '0', 'msg': '成功'}
    #     for i in range(len(product_key)):
    #         link_add = add_product(self, node_ip_port=product_key[i], results=result_add)
    #         print("新增链路" + product_key[i] +":"+ str(link_add))
    #     # step5 获取token
    #     token = get_token(self, self.head_get_token)['result']
    #     print('step5 获取token：' + str(token))
    #     # step6 申请提速
    #     result6 = {'msg': '成功', 'code': '0'}
    #     r = speeding(self, self.head, token, )
    #     print('step6 申请提速:' + str(r))
    #
    # def test_13_add_with_wrong_node_ip_port(self):
    #     '''动态新增时，传入的node_ip_port错误'''
    #     node_ip_port = '192.168.203.1:10002'
    #     result = {"code":"10000","msg":"对不起，系统异常"}
    #     a = add_product(self,node_ip_port=node_ip_port,results=result)
    #     print('使用错误的node_ip_port动态新增链路：'+ str(a))
    #
    # def test_14_add_with_wrong_remote_ip_port(self):
    #     '''动态新增时，传入的remote_ip_port错误'''
    #     remote_ip_port = '192.168.203.1:10002'
    #     result = {"code":"10000","msg":"对不起，系统异常"}
    #     a = add_product(self,remote_ip_port=remote_ip_port,results=result)
    #     print('使用错误的remote_ip_port动态新增链路：'+ str(a))
    #
    # def test_15_add_with_wrong_remote_hostname(self):
    #     '''动态新增时，传入的remote_hostname错误'''
    #     remote_hostname = 'abc'
    #     result = {"code":"10000","msg":"对不起，系统异常"}
    #     a = add_product(self,remote_hostname=remote_hostname,results=result)
    #     print('使用错误的remote_hostname动态新增链路：'+ str(a))
    #
    # def test_16_add_with_notmatch_remote_hostname_and_remote_ip_port(self):
    #     '''动态新增时，传入的remote_hostname与remote_ip_port不匹配'''
    #     remote_hostname = 'abc'
    #     remote_ip_port = '192.168.203.1:10002'
    #     result = {"code":"10000","msg":"对不起，系统异常"}
    #     a = add_product(self,remote_hostname=remote_hostname,remote_ip_port=remote_ip_port,results=result)
    #     print('使用不匹配的remote_hostname与remote_ip_port动态新增链路：'+ str(a))


if __name__ == "__main__":
    unittest.main()
