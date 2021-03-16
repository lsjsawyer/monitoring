# -*- coding: utf-8 -*-
from basic.get_ip_port import get_ip_port
from basic.protobuf_translation import protobuf_translation
from basic.socket_request_way import socket_get_way
from socket_package import socket_package
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from basic.push_dingding import msg


def A_load_9_15():
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #9点15,level1上证大盘
    re_1 = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_ss_zs_socket_package)
    result_1 = protobuf_translation(re_1)
    if "trends" and "min_time" and "last_px" and "0915" in result_1:
        print("level1,上证指数正在推送,%s" % time_now)
    else:
        push_data_13 = "上证指数level1异常: %s" % time_now
        msg(push_data_13)
        print("上证指数level1异常: %s" % time_now)
    #9点15, level1上证个股
    re_2 = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_ss_socket_package)
    result_2 = protobuf_translation(re_2)
    if "trends" and "min_time" and "last_px" and "0915" in result_2:
        print("level1,上证个股正在推送,%s" % time_now)
    else:
        push_data_2 = "上证个股level1异常: %s" % time_now
        msg(push_data_2)
        print("上证个股level1异常: %s" % time_now)
    # 9点15,level1 科创股票
    re_3 = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_ss_kc_socket_package)
    result_3 = protobuf_translation(re_3)
    if "trends" and "min_time" and "last_px" and "0915" in result_3:
        print("level1,科创股票正在推送,%s" % time_now)
    else:
        push_data_3 = "科创股票level1异常: %s" % time_now
        msg(push_data_3)
        print("科创股票level1异常: %s" % time_now)
    # 9点15,level1 深证大盘
    re_4 = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_sz_zs_socket_package)
    result_4 = protobuf_translation(re_4)
    if "trends" and "min_time" and "last_px" and "0915" in result_4:
        print("level1,深证大盘正在推送,%s" % time_now)
    else:
        push_data_4 = "深证大盘level1异常: %s" % time_now
        msg(push_data_4)
        print("深证大盘level1异常: %s" % time_now)
    # 9点15,level1 深证个股
    re_5 = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_sz_socket_package)
    result_5 = protobuf_translation(re_5)
    if "trends" and "min_time" and "last_px" and "0915" in result_5:
        print("level1,深证个股正在推送,%s" % time_now)
    else:
        push_data_5 = "深证个股level1异常: %s" % time_now
        msg(push_data_5)
        print("深证个股level1异常: %s" % time_now)
    # 9点15,level1 创业版
    re_6 = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_sz_cy_socket_package)
    result_6 = protobuf_translation(re_6)
    if "trends" and "min_time" and "last_px" and "0915" in result_6:
        print("level1,创业版正在推送,%s" % time_now)
    else:
        push_data_6 = "创业版level1异常: %s" % time_now
        msg(push_data_6)
        print("创业版level1异常: %s" % time_now)
    # 9点15,level2 上证指数
    re_7 = socket_get_way(get_ip_port()[2], int(get_ip_port()[3]), socket_package.level2_ss_zs_socket_package)
    result_7 = re_7.decode()
    if "trendData" and "0915" in result_7:
        print("level2,上证大盘推送正常,%s" % time_now)
    else:
        push_data_7 = "上证大盘level2异常: %s" % time_now
        msg(push_data_7)
        print("上证大盘level2异常: %s" % time_now)
    # 9点15,level2 上证个股
    re_8 = socket_get_way(get_ip_port()[2], int(get_ip_port()[3]), socket_package.level2_ss_socket_package)
    result_8 = re_8.decode()
    if "trendData" and "0915" in result_8:
        print("level2,上证个股推送正常,%s" % time_now)
    else:
        push_data_8 = "上证个股level2异常: %s" % time_now
        msg(push_data_8)
        print("上证个股level2异常: %s" % time_now)
    # 9点15,level2 科创版
    re_9 = socket_get_way(get_ip_port()[2], int(get_ip_port()[3]), socket_package.level2_ss_kc_socket_package)
    result_9 = re_9.decode()
    if "trendData" and "0915" in result_9:
        print("level2,科创版推送正常,%s" % time_now)
    else:
        push_data_9 = "科创版level2异常: %s" % time_now
        msg(push_data_9)
        print("科创版level2异常: %s" % time_now)
    # 9点15,level2 深证大盘
    re_10 = socket_get_way(get_ip_port()[4], int(get_ip_port()[5]), socket_package.level2_sz_zs_socket_package)
    result_10 = re_10.decode()
    if "trendData"and "0915" in result_10:
        print("level2,深证大盘推送正常,%s" % time_now)
    else:
        push_data_10 = "深证大盘level2异常: %s" % time_now
        msg(push_data_10)
        print("深证大盘level2异常: %s" % time_now)
    # 9点15,level2 深证个股
    re_11 = socket_get_way(get_ip_port()[4], int(get_ip_port()[5]), socket_package.level2_sz_socket_package)
    result_11 = re_11.decode()
    if "trendData"and "0915" in result_11:
        print("level2,深证个股推送正常,%s" % time_now)
    else:
        push_data_11 = "深证个股level2异常: %s" % time_now
        msg(push_data_11)
        print("深证个股level2异常: %s" % time_now)
    # 9点15,level2 创业版
    re_12 = socket_get_way(get_ip_port()[4], int(get_ip_port()[5]), socket_package.level2_sz_cy_socket_package)
    result_12 = re_12.decode()
    if "trendData" and "0915" in result_12:
        print("level2,创业版推送正常,%s" % time_now)
    else:
        push_data_12 = "创业版level2异常: %s" % time_now
        msg(push_data_12)
        print("创业版level2异常: %s" % time_now)

scheduler2 = BlockingScheduler()
scheduler2.add_job(A_load_9_15, 'cron', day_of_week='1-5', hour=9, minute=16)
scheduler2.start()

