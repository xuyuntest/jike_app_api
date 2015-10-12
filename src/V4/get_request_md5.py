#coding=utf-8

import urllib2,urllib,httplib
import json
import sys, os
import hashlib
import uuid
import datetime

nonce = str(uuid.uuid1())[0:8]
from_version = '1-4.2.2-2.0.0'
timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
api_key = 'uyW3d8Fu'
api_secret = 'uyW3d8FuKISUE911CHN'
channel = 'jikexueyuan'
token='a93148d5473806d5ac4b47c0a43407dc'
#api_sig_old=nonce+timestamp+api_key+api_secret+token
#print api_sig_old
uid = '3574506';
#3574506
api_sig_old_token='525d5036'+'20150813104621'+'uyW3d8Fu'+'uyW3d8FuKISUE911CHN'+'a93148d5473806d5ac4b47c0a43407dc'






def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

api_sig = md5(api_sig_old_token)

#parames = '?nonce='+nonce+'&from='+from_version+'&timestamp='+timestamp+'&api_key='+api_key+'&channel='+channel+'&api_sig='+api_sig

parames = '?'+'debug=eNIgma'+'&nonce='+'525d5036'+'&from='+'1-5.0.1-2.4.0'+'&timestamp='+'20150813104621'+'&api_key='+api_key+'&channel='+'jkxiaomi_pt_sd_1_2.4.0_101'+'&api_sig='+api_sig+'&uid='+uid

#print parames

req_url1 =  'http://api.jikexueyuan.com/v3/msg/read'
req_url2 =  parames
req_url  = req_url1+req_url2

print req_url


