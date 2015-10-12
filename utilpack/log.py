__author__ = 'yun'


import logging
import time


local_time = time.strftime("%Y%m%d")
#print local_time


def print_log_sessuce(filename):
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s'+' '+filename+' '+' %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename='/Users/yun/PycharmProjects/jikexueyuan/log/'+local_time+'.log',
                filemode='a+')

#logging.debug('This is debug message')
    logging.info('The result is true')
#logging.warning('This is warning message')


def print_log_fail(filename,response):
    logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s'+' '+filename+' '+'[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                filename='/Users/yun/PycharmProjects/jikexueyuan/log/'+local_time+'.log',
                filemode='a+')

#logging.debug('This is debug message')
    logging.info('The result is fail'+'\n'+response)
#logging.warning('This is warning message')


#print_log_sessuce('test.py')