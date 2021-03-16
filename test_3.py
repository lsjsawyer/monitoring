# -*- coding: utf-8 -*-
from basic.protobuf_translation import protobuf_translation
from basic.socket_request_way import socket_get_way


socket_1 = '{"channel":{"version":"2.0","sub":"l1basic","unsub":""},' \
                             '"user":{"id":"","sign":"91529d7d5a6303d286877bfb5dcd6484",' \
                             '"device_id":"2019-12-18 15:58:33.477421 +0800 CST m=+0.109975980","ts":"1573733347"},' \
                             '"params":{"l1basic":{"encoding":"pb","min_time":"","stock_code":"GN0791.XBHS", ' \
                             '"need_index_callauction": "1"}}}\n'

re_7 = socket_get_way("47.96.178.66", 8008, socket_1)  #测试47.96.178.66  生产121.41.29.58
re = protobuf_translation(re_7)
print(re)
