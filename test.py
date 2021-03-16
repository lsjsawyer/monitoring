# -*- coding: utf-8 -*-
#author tom
import time
from distutils.log import Log

from basic.get_ip_port import get_ip_port
from socket_package import socket_package
import datetime

# print(str(int(time.time())))
#
# r = {"data": {"level1": ["121.41.29.58:8008"], "level2": ["121.41.24.33:8601"], "level2SZ": ["121.41.24.33:8601"]},
#      "first": "true", "status": 200, "topic": "l2-notice", "type": "notice"}
#
# print(r["data"]["level1"][0][-4:])
# print(r["data"]["level1"][0][:-5])


# from apscheduler.schedulers.blocking import BlockingScheduler
# from datetime import datetime
import socket
from pb_file import l1basic_pb2

# def job():
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# # BlockingScheduler
# scheduler = BlockingScheduler()
# scheduler.add_job(job, 'cron', day_of_week='1-5', hour=9, minute=58)
# scheduler.start()
#
# job()
# 人肉看，A股，上海，深圳，创业板，科创板  的股票
# 121.41.29.58:8008
#
# Host = "121.41.29.58"
# port = 8008
# list = []
# def clean_data():
#     level1_ss_url = '{"channel":{"version":"2.0","sub":"l1basic","unsub":""},' \
#                     '"user":{"id":"","sign":"91529d7d5a6303d286877bfb5dcd6484",' \
#                     '"device_id":"2019-12-18 15:58:33.477421 +0800 CST m=+0.109975980","ts":"1573733347"},' \
#                     '"params":{"l1basic":{"encoding":"json","min_time":"","stock_code":"000001.SS", ' \
#                     '"need_index_callauction": "1"}}}\n'
#     level2_ss_url = ""
#     cline = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     cline.connect((Host, port))
#     cline.sendall(level1_ss_url.encode('utf8'))
#     recive_data = cline.recv(1024 * 1000)
#     quan_data = recive_data[8:]
#     pb = l1basic_pb2.l1BasicResponse()
#     pb.ParseFromString(quan_data)
#     result = "%s" % pb
#     if "trends" and "min_time" and "last_px" and "0915" in result:
#         print("存在分时")
#     else:
#         print("不存在")
#     # print(result)
#
# clean_data()
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

import requests
import json

def dingTalk():
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    values = {
        "msgtype": "text",
        "text": {
            "content": "监控:hello"
        }
    }
    json_data = json.dumps(values)
    requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=2145e5f2c38489b83a59ab04c4f1bef48421ffe30a5b2df8b7bccbc78f2f0326',data=json_data,headers=header)


# import time
# import hmac
# import hashlib
# import base64
# import urllib.parse
#
# timestamp = str(round(time.time() * 1000))
# secret = 'this is a secret'
# secret_enc = secret.encode('utf-8')
# string_to_sign = '{}\n{}'.format(timestamp, secret)
# string_to_sign_enc = string_to_sign.encode('utf-8')
# hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
# sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
# print(timestamp)
# print(sign)
#
# curl 'https://oapi.dingtalk.com/robot/send?access_token=ac0419d2f171743866269a3a8762b801fb52fe646ba6cec330b35cc01e7cbea0' \
#    -H 'Content-Type: application/json' \
#    -d '{"msgtype": "text","text": {"content": "监控"}}'