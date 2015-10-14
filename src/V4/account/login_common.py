#coding=utf-8
'''
Created on 2015-5-29
@author: yun.xu
'''
import sys,os
sys.path.append("/Users/yun/PycharmProjects/jikexueyuan")
from utilpack import check_response
from utilpack import http_request


'''
#公共参数

from_version
channel
timestamp
nonce
api_key
api_sig
'''

#request
req_typy = "POST"
req_data = "uname=ssfggg019@163.com&password=111111"
req_url =  "http://api.jikexueyuan.com/v3/account/login_common?nonce=eb52587a&from=1-4.2.2-2.0.0&timestamp=20150603114504&api_key=uyW3d8Fu&channel=jikexueyuan&api_sig=5b17f4e447db4db5ace7afe901f8e406"
req_host = "api.jikexueyuan.com"

#response
expect1 = '200'
expect2 = 'ok'
expect3 = '3574506'

def __init__(self):
        pass

if __name__ == '__main__':
    case_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
    response = http_request.getURL(req_typy,req_data,req_url,req_host)
    check_response.checkResult(response,case_name,expect1,expect2,expect3)
    pass
