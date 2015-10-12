#coding=utf-8
'''
Created on 2015-5-29
@author: yun.xu
'''
import sys,os
sys.path.append("/Users/yun/PycharmProjects/jikexueyuan")
from utilpack import check_response
from utilpack import http_request

req_typy = "POST"
req_data = "uid=3610571&like=0&cid=524"
req_url =  "http://api.jikexueyuan.com/v3/user/set_like_course?api_key=uyW3d8Fu&api_sig=25cd5973e5c85431fea9825a1e8acf65&uid=3610571&from=1-5.0.1-2.4.0&timestamp=20150813114510&nonce=824d52c3&channel=jkxiaomi_pt_sd_1_2.4.0_101"
req_host = "api.jikexueyuan.com"

#response
expect1 = '200'
expect2 = 'ok'
expect3 = ''

def __init__(self):
        pass

if __name__ == '__main__':
    case_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
    response = http_request.getURL(req_typy,req_data,req_url,req_host)
    check_response.checkResult(response,case_name,expect1,expect2,expect3)
    pass
