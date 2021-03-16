from apscheduler.schedulers.blocking import BlockingScheduler


def a():
    print("A")

def b():
    print("B")

def c():
    print("C")

scheduler3 = BlockingScheduler()
s1 = scheduler3.add_job(a, 'cron', day_of_week='1-5', hour=17, minute=19)
s1.remove()
s2 = scheduler3.add_job(b, 'cron', day_of_week='1-5', hour=16, minute=20)
s2.resume()
s3 = scheduler3.add_job(c, 'cron', day_of_week='1-5', hour=16, minute=21)
s3.remove()


scheduler3.start()



