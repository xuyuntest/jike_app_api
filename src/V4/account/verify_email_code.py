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
req_data = "email=ssfggg@163.com&type=3"
req_url =  "http://api.jikexueyuan.com/v3/account/verify_email_code?nonce=86cc6880&from=1-4.2.2-2.0.0&timestamp=20150603113506&api_key=uyW3d8Fu&channel=jikexueyuan&api_sig=9a0b8436ae000a62de68e79e68faba96"
req_host = "api.jikexueyuan.com"



#response
expect1 = '200'
expect2 = '激活邮件已发送至你的邮箱'
expect3 = 'true'

def __init__(self):
        pass

if __name__ == '__main__':
    case_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
    response = http_request.getURL(req_typy,req_data,req_url,req_host)
    check_response.checkResult(response,case_name,expect1,expect2,expect3)
    pass

