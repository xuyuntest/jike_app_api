#coding=utf-8
__author__ = 'yun'

'''
Created on 2015-5-29
@author: yun.xu
'''

import httplib
import json
#import demjson

def getURL(req_typy,req_data,req_url,req_host):

    data = req_data
    #data_urlencode = urllib.urlencode(data)
    #print data
    requrl = req_url
    headerdata = {'Content-type': 'application/x-www-form-urlencoded'}
    con = httplib.HTTPConnection(req_host)
    con.request(method= req_typy,url=requrl,body=data,headers=headerdata)
    response = con.getresponse()
    res= response.read()
    #print type(res);
    print res;
#需要加入res为空的异常判断
    if(res != ''):
        #res = demjson.decode(res)
        return res;
    else:
        i = ''
        return i;


