import datetime
import os
import glob


files = glob.glob('C:/Users/Oguz/Desktop/New folder/*')
for f in files:
    os.remove(f)


DayL = ['Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur', 'Sun']
date = DayL[datetime.date(2022, 1, 12).weekday()] + 'day'
print(date)
