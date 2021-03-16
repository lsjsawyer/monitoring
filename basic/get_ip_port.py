# -*- coding: utf-8 -*-
import socket
import time
import ast

# 返回顺序:level1host levelport level2host level2port leve2SZhost level2SZport
def get_ip_port():
    timestamp = str(int(time.time()*1000))
    po = '{"channel": {"topic": "l2-notice", "type": "notice"}, "action": "sub",' \
         ' "user": {"id": "1235"}, "params": {"timestamp": "'+timestamp+'"}}\n'
    host = "47.98.129.69"
    port = 8019
    BufferSize = 1024 * 1000
    coon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    coon.connect((host, port))
    coon.sendall(po.encode('utf8'))
    re = coon.recv(BufferSize).decode()
    re_dict = ast.literal_eval(re)
    level_1_host = re_dict["data"]["level1"][0][:-5]
    level_1_port = re_dict["data"]["level1"][0][-4:]
    level_2_host = re_dict["data"]["level2"][0][:-5]
    level_2_port = re_dict["data"]["level2"][0][-4:]
    level_2SZ_host = re_dict["data"]["level2SZ"][0][:-5]
    level_2SZ_port = re_dict["data"]["level2SZ"][0][-4:]
    return level_1_host, level_1_port, level_2_host, level_2_port, level_2SZ_host, level_2SZ_port


