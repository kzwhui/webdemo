#!/usr/bin/python
#encoding=utf8

import sys
import cgi
import traceback
import json
import re
import random
sys.path.append('../common/')
sys.path.append('../conf/')
from log import logger
from conf import g_conf
from db_wrapper import DBWrapperFactory

def get_img_url(ret_root):
    sql = "select distinct c_url, c_description from t_image_url limit 200"
    rows = DBWrapperFactory.get_instance('d_web_demo').get_dict(sql)
    img_list = []
    for row in rows:
        img = {}
        img['src'] = row['c_url']
        img['description'] = row['c_description']
        img_list.append(img)
    random.shuffle(img_list)

    ret_root['data'] = img_list

def main_proc(ret_root):
    requests = cgi.FieldStorage()
    flag = requests.getvalue('flag')

    if flag == '0':
        get_img_url(ret_root)
    else:
        logger.error('flag error, flag = %s' % (flag))
        ret_root['ret'] = -1
        ret_root['msg'] = u'输入的搜索类型不合法'

if __name__ == '__main__':
    logger.info('cgi begin')
    ret_root = {"ret":0, 'data':{}, 'msg':''}
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