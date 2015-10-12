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
req_url =  "http://api.jikexueyuan.tv/v3/search/course?debug=eNIgma&api_key=uyW3d8Fu&api_sig=ff8ab59f3f6300fe6df4503fb5e99f40&num=10&uid=3491060&from=1-5.0.1-2.4.0&page=1&type=course&word=iOS&timestamp=20150824171220&noUid=false&nonce=807c199f&channel=jkxiaomi_pt_sd_1_2.4.0_101&needUid=1"
req_host = "api.jikexueyuan.com"

#response
expect1 = '200'
expect2 = '查询成功'
expect3 = '119'

def __init__(self):
        pass

if __name__ == '__main__':
    case_name = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
    response = http_request.getURL(req_typy,req_data,req_url,req_host)
    check_response.checkResult(response,case_name,expect1,expect2,expect3)
    pass
