import datetime

now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

future_date = datetime.datetime(2027, 1, 1)
difference = future_date - now
print(difference.days)