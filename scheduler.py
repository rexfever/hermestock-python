import schedule
import time
import hermes


def job():
    hermes.job()


# schedule.every().minute.do(job)
schedule.every().days.at("15:45").do(job)

while True:
    print(f'{time.localtime().tm_year}.{time.localtime().tm_mon}.{time.localtime().tm_mday} {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}')
    now = time.localtime().tm_wday
    if now != 5 and now != 6:
        schedule.run_pending()
        time.sleep(1)
