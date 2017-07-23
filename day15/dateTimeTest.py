# coding:UTF-8
from datetime import datetime

now=datetime.now()#获取当前时间
print now
print (type(now))

dt=datetime(2014,3,2,2,3,4)
print dt

# str和 datetime的互换
cday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print cday
print (datetime.now().strftime('%a-%b-%d %H:%M'))

#dateTime的加减
from datetime import timedelta
print datetime.now()+timedelta(days=1)
print datetime.now()+timedelta(hours=1)

#调整市区
# from datetime import timezone
# tz_ut_8=timezone(timedelta(hours=8))

import re
print re.match(r'^UTC[+,-](\d):\d{2}','UTC-5:00').group(1)
