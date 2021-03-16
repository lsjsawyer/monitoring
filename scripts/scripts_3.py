# -*- coding: utf-8 -*-

from basic.push_dingding import msg
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
def over_remind():
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    push_data = "代码已运行: %s" % time_now
    msg(push_data)
    print("代码已运行: %s" % time_now)

scheduler3 = BlockingScheduler()
scheduler3.add_job(over_remind, 'cron', day_of_week='1-5', hour=16, minute=50)
scheduler3.start()
