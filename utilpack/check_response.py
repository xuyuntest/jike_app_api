#coding=utf-8
'''
Created on 2015-5-29
@author: yun.xu
'''
import log
import json


def checkResult(response,case_name,expect1,expect2,expect3):


#需要加入response为空是的异常判断
    if(response != ''):
        if(response.find(str(expect1))>0 and response.find(str(expect2))>0 and response.find(str(expect3))>0):
            log.print_log_sessuce(case_name)
        else:
            #print html["IsError"]
            log.print_log_fail(case_name,response)
    else:
        log.print_log_fail(case_name)
    pass

