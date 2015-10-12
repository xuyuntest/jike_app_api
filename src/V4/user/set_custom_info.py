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
req_data = "uid=3610571&cate_id=1&experience=1"
req_url =  "http://api.jikexueyuan.com/v3/user/set_custom_info?api_key=uyW3d8Fu&api_sig=e86519a132eef21eec81bc2e68c78573&uid=3610571&from=1-5.0.1-2.4.0&timestamp=20150813112329&nonce=43aa6d5f&channel=jkxiaomi_pt_sd_1_2.4.0_101"
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
