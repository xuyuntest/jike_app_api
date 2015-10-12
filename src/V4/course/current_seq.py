#coding=utf-8
'''
Created on 2015-5-29
@author: yun.xu
'''
import sys,os
sys.path.append("/Users/yun/PycharmProjects/jikexueyuan")
from utilpack import check_response
from utilpack import http_request

req_typy = "GET"
req_data = ""
req_url =  "http://api.jikexueyuan.com/v3/course/current_seq?debug=eNIgma&api_key=uyW3d8Fu&api_sig=44b693052971b0f3eea42b9b831ab55d&uid=3574506&cid=119&seq=2&from=1-5.0.1-2.4.0&timestamp=20150824174335&noUid=false&nonce=f7019b01&channel=jkxiaomi_pt_sd_1_2.4.0_101"
req_host = "api.jikexueyuan.com"

#response
expect1 = '200'
expect2 = 'ok'
expect3 = '"status":1'

def __init__(self):
        pass

if __name__ == '__main__':
    case_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
    response = http_request.getURL(req_typy,req_data,req_url,req_host)
    check_response.checkResult(response,case_name,expect1,expect2,expect3)
    pass
