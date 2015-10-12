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
req_url =  "http://api.jikexueyuan.com/v3/course/favorite_do?debug=eNIgma&status=1&api_key=uyW3d8Fu&api_sig=237ac7b0ce9c7c8148bd905a498dedb1&cid=119&uid=3574506&from=1-5.0.1-2.4.0&timestamp=20150824171815&noUid=false&nonce=74462a57&channel=jkxiaomi_pt_sd_1_2.4.0_101"
req_host = "api.jikexueyuan.com"

#response
expect1 = '200'
expect2 = '已添加收藏'
expect3 = '"cate_id":"60"'

def __init__(self):
        pass

if __name__ == '__main__':
    case_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
    response = http_request.getURL(req_typy,req_data,req_url,req_host)
    check_response.checkResult(response,case_name,expect1,expect2,expect3)
    pass
