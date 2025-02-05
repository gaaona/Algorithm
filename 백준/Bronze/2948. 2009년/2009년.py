import datetime
import sys

day_input, month_input = map(int, sys.stdin.readline().split())

weekday_num = datetime.date(2009, month_input, day_input).isoweekday()
if weekday_num == 1:
    print("Monday")
elif weekday_num == 2:
    print("Tuesday")
elif weekday_num == 3:
    print("Wednesday")
elif weekday_num == 4:
    print("Thursday")
elif weekday_num == 5:
    print("Friday")
elif weekday_num == 6:
    print("Saturday")
elif weekday_num == 7:
    print("Sunday")