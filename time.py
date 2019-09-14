import datetime

"""ty=datetime.date(2015,7,30)
print(ty)


tdelta=datetime.timedelta(days=10)
print(tdelta.days)
"""

bday=datetime.date(1999,8,2)
print(bday)
tday=datetime.date.today()
print(tday)

tdelta1=bday-tday
print(tdelta1.total_seconds())

