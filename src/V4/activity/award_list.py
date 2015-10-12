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
req_url =  "http://api.jikexueyuan.com/v3/activity/award_list?debug=eNIgma&nonce=525d5036&from=1-5.0.1-2.4.0&timestamp=20150813104621&api_key=uyW3d8Fu&channel=jkxiaomi_pt_sd_1_2.4.0_101&api_sig=5a71a3e94016c6c7fd0d0a3b3408d93c&uid=3574506"
req_host = "api.jikexueyuan.com"

#response
expect1 = '200'
expect2 = 'ok'
expect3 = '登录领取5天VIP'


def __init__(self):
        pass

if __name__ == '__main__':
    case_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
    response = http_request.getURL(req_typy,req_data,req_url,req_host)
    check_response.checkResult(response,case_name,expect1,expect2,expect3)
    pass
