import os
import glob
import schedule
import time


def job():
    files = glob.glob('C:/Users/Oguz/Desktop/New folder/*')
    for f in files:
        os.remove(f)


schedule.every().friday.at("07:01").do(job)
schedule.every().friday.at("17:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)