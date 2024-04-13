import datetime
today=datetime.datetime(2024,2,15,12,0,0)
mybithday=datetime.datetime(1998,9,11,0,0,0)
mylife=today-mybithday
timedelta_days=mylife.days
print("Type of mylife is :", type(mylife))
print("Type of days is: ", type(timedelta_days))
print(mylife)
print(timedelta_days)