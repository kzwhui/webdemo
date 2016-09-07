#!/usr/bin/python
#encoding=utf8

import sys
import cgi
import traceback
import json
import re
sys.path.append('../common/')
sys.path.append('../conf/')
from log import logger
from conf import g_conf

def main_proc(ret_root):
    requests = cgi.FieldStorage()
    name = requests.getvalue('name')
    ret_root['data']['name'] = name

if __name__ == '__main__':
    logger.info('cgi begin')
    ret_root = {"ret":0, 'data':{}}
    header = "Content-type: application/json\n"
    print header
    try:
        main_proc(ret_root)
    except:
        logger.error(traceback.format_exc())
        ret_root['ret'] = -1
        ret_root['msg'] = '发生异常'
    callback = cgi.FieldStorage().getvalue("callback")
    reg = re.compile('^[\w_]+$')
    if callback and reg.search(callback):
        print callback + "(" + json.dumps(ret_root) + ")"
    else:
        print json.dumps(ret_root)
    logger.info('cgi end')