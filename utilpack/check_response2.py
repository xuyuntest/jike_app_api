#coding=utf-8
'''
Created on 2015-5-29
@author: yun.xu
'''

from util import log
import json


def checkResult(response,case_name):

    #json_dict_key = response.get('data').get('user')
    #print json_dict_key['uid'];

#需要加入response为空是的异常判断
    if(response != ''):
        if response['code'] == 200:
            #print html["IsError"]
            log.print_log_sessuce(case_name)

        else:
            #print html["IsError"]
            log.print_log_fail(case_name)
    else:
        log.print_log_fail(case_name)
    pass

