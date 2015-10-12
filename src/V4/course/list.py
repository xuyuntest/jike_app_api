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
req_url =  "http://api.jikexueyuan.com/v3/course/list?api_key=uyW3d8Fu&api_sig=4e9488cddb27d1fb47ed48a27c832f53&n=10&p=1&flag=1&free=0&from=1-5.0.1-2.4.0&type=0&timestamp=20150813102852&level=0&nonce=cc939228&cate_id=1&channel=jkxiaomi_pt_sd_1_2.4.0_101"
req_host = "api.jikexueyuan.com"

#response
expect1 = '200'
expect2 = 'ok'
expect3 = '51'


def __init__(self):
        pass

if __name__ == '__main__':
    case_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
    response = http_request.getURL(req_typy,req_data,req_url,req_host)
    check_response.checkResult(response,case_name,expect1,expect2,expect3)
    pass
