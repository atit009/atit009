#!/usr/bin/env python3
import calendar
# print (calendar.TextCalendar(firstweekday=6).formatyear(2015))
inp=list(map(int, input().split()))
MONTH=inp[0]
DAY=inp[1]
YEAR=inp[2]
C=(calendar.weekday(YEAR,MONTH,DAY))
# print(C)
a=(calendar.month(YEAR, MONTH,DAY))
# print(a)
# print(type(a))
Days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(Days[C])

