from basic.get_ip_port import get_ip_port
from basic.protobuf_translation import protobuf_translation
from basic.socket_request_way import socket_get_way
from socket_package import socket_package
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from basic.push_dingding import msg

def level_1_SS():
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 9点,level1上证大盘
    re = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_ss_zs_socket_package)
    result = protobuf_translation(re)
    if "trends" and "min_time" and "last_px" and "0915" not in result:
        print("level1,上证指数已经清理,%s" % time_now)
    else:
        push_data = "上证指数level1清理异常: %s" % time_now
        msg(push_data)
        print("上证指数level1清理异常: %s" % time_now)
    # 9点,level1上证个股
    re = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_ss_socket_package)
    result = protobuf_translation(re)
    if "trends" and "min_time" and "last_px" and "0915" not in result:
        print("level1,上证个股已经清理,%s" % time_now)
    else:
        push_data = "上证个股level1清理异常: %s" % time_now
        msg(push_data)
        print("上证个股level1清理异常: %s" % time_now)
    # 9点,level1 科创股票
    re = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_ss_kc_socket_package)
    result = protobuf_translation(re)
    if "trends" and "min_time" and "last_px" and "0915" not in result:
        print("level1,科创股票已经清理,%s" % time_now)
    else:
        push_data = "科创股票level1清理异常: %s" % time_now
        msg(push_data)
        print("科创股票level1清理异常: %s" % time_now)
    # 9点,level1 深证大盘
    re = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_sz_zs_socket_package)
    result = protobuf_translation(re)
    if "trends" and "min_time" and "last_px" and "0915" not in result:
        print("level1,深证大盘已经清理,%s" % time_now)
    else:
        push_data = "深证大盘level1清理异常: %s" % time_now
        msg(push_data)
        print("深证大盘level1清理异常: %s" % time_now)
    # 9点,level1 深证个股
    re = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_sz_socket_package)
    result = protobuf_translation(re)
    if "trends" and "min_time" and "last_px" and "0915" not in result:
        print("level1,深证个股已经清理,%s" % time_now)
    else:
        push_data = "深证个股level1清理异常: %s" % time_now
        msg(push_data)
        print("深证个股level1清理异常: %s" % time_now)
    # 9点,level1 创业版
    re = socket_get_way(get_ip_port()[0], int(get_ip_port()[1]), socket_package.level1_sz_cy_socket_package)
    result = protobuf_translation(re)
    if "trends" and "min_time" and "last_px" and "0915" not in result:
        print("level1,创业版已经清理,%s" % time_now)
    else:
        push_data = "创业版level1清理异常: %s" % time_now
        msg(push_data)
        print("创业版level1清理异常: %s" % time_now)
    # 9点,level2 上证指数
    re = socket_get_way(get_ip_port()[2], int(get_ip_port()[3]), socket_package.level2_ss_zs_socket_package)
    result = re.decode()
    if "trendData" and "0915" not in result:
        print("level2,上证大盘已经清理,%s" % time_now)
    else:
        push_data = "上证大盘level2清理异常: %s" % time_now
        msg(push_data)
        print("上证大盘level2清理异常: %s" % time_now)
    # 9点,level2 上证个股
    re = socket_get_way(get_ip_port()[2], int(get_ip_port()[3]), socket_package.level2_ss_socket_package)
    result = re.decode()
    if "trendData" and "0915" not in result:
        print("level2,上证个股已经清理,%s" % time_now)
    else:
        push_data = "上证个股level2清理异常: %s" % time_now
        msg(push_data)
        print("上证个股level2清理异常: %s" % time_now)
    # 9点,level2 科创版
    re = socket_get_way(get_ip_port()[2], int(get_ip_port()[3]), socket_package.level2_ss_kc_socket_package)
    result = re.decode()
    if "trendData" and "0915" not in result:
        print("level2,科创版已经清理,%s" % time_now)
    else:
        push_data = "科创版level2清理异常: %s" % time_now
        msg(push_data)
        print("科创版level2清理异常: %s" % time_now)
    # 9点,level2 深证大盘
    re = socket_get_way(get_ip_port()[4], int(get_ip_port()[5]), socket_package.level2_sz_zs_socket_package)
    result = re.decode()
    if "trendData"and "0915" not in result:
        print("level2,深证大盘已经清理,%s" % time_now)
    else:
        push_data = "深证大盘level2清理异常: %s" % time_now
        msg(push_data)
        print("深证大盘level2清理异常: %s" % time_now)
    # 9点,level2 深证个股
    re = socket_get_way(get_ip_port()[4], int(get_ip_port()[5]), socket_package.level2_sz_socket_package)
    result = re.decode()
    if "trendData"and "0915" not in result:
        print("level2,深证个股已经清理,%s" % time_now)
    else:
        push_data = "深证个股level2清理异常: %s" % time_now
        msg(push_data)
        print("深证个股level2清理异常: %s" % time_now)
    # 9点,level2 创业版
    re = socket_get_way(get_ip_port()[4], int(get_ip_port()[5]), socket_package.level2_sz_cy_socket_package)
    result = re.decode()
    if "trendData" and "0915" not in result:
        print("level2,创业版已经清理,%s" % time_now)
    else:
        push_data = "创业版level2清理异常: %s" % time_now
        msg(push_data)
        print("创业版level2清理异常: %s" % time_now)

scheduler1 = BlockingScheduler()
scheduler1.add_job(level_1_SS, 'cron', day_of_week='1-5', hour=20, minute=52)
scheduler1.start()


