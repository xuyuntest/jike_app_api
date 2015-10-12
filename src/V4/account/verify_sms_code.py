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
req_data = "phone=15810557815&type=6"
#req_url =  "http://api.jikexueyuan.com/v3/account/verify_sms_code?nonce=12fe0d42&from=1-4.2.2-2.0.0&timestamp=20150529095405&api_sig=0196f2142c951135e81caa2391853f77&api_key=uyW3d8Fu&channel=jikexueyuan"
req_url =  "http://api.jikexueyuan.com/v3/account/verify_sms_code?nonce=d508de9c&from_version=1-4.2.2-2.0.0&timestamp=20150602201352&api_key=uyW3d8Fu&channel=jikexueyuan&api_sig=8cc36e98df1ef3589d00c515ccb9cba7"
req_host = "api.jikexueyuan.com"



#response
expect1 = '200'
expect2 = '短信提交成功'
expect3 = 'true'

def __init__(self):
        pass

if __name__ == '__main__':
    case_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
    response = http_request.getURL(req_typy,req_data,req_url,req_host)
    check_response.checkResult(response,case_name,expect1,expect2,expect3)
    pass
