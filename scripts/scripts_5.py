# -*- coding: utf-8 -*-
from basic.get_ip_port import get_ip_port
from basic.protobuf_translation import protobuf_translation
from basic.socket_request_way import socket_get_way
from socket_package import socket_package
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from basic.push_dingding import msg


def level_1_SS_GG():
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 9点,level1上证个股
    re = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_ss_socket_package)
    result = protobuf_translation(re)
    if "trends" and "min_time" and "last_px" and "0915" not in result:
        print("level1,上证个股已经清理,%s" % time_now)
    else:
        push_data = "上证个股level1清理异常: %s" % time_now
        msg(push_data)
        print("上证个股level1清理异常: %s" % time_now)


scheduler1 = BlockingScheduler()
scheduler1.add_job(level_1_SS_GG, 'cron', day_of_week='1-5', hour=18, minute=3)
scheduler1.start()