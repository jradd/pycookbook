'Python Dates'

from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b

print(c.days)
# be aware: there is no hours
print(c.seconds)
hours = c.seconds/3600
print(hours)
print(c.total_seconds())


from datetime import datetime
a = datetime(2014,11,11)
print(a+ timedelta(days=10))
# date,  + some days
print(type(a+ timedelta(days=10)))
b = datetime(2015,3,1)

# datediff, days
print(b-a)

# later- easier, or easier - later
print(datetime(2014,1,1)-datetime(2014,2,2))


# months is invalid argument
# print(a+timedelta(months=1))



# about date + - recomment use another module

#

from dateutil.relativedelta import relativedelta

b = a + relativedelta(months=+1)
print(b)
print(a+relativedelta(months=+4))
print(a+relativedelta(months=-3))

print(b-a)
d = datetime(2015,3,1)

print(relativedelta(d,a))


'Determining Last Fredays Date'

from datetime import datetime, timedelta

weekdays = ['Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday']

start_date = datetime.today()
day_num = start_date.weekday()
print(day_num) # Monday 0 ?

def get_previous_byday(dayname, start_date=None):
	if start_date is None:
		start_date = datetime.today()
	day_num = start_date.weekday()
	day_num_target = weekdays.index(dayname) # such Thurs: 3
	days_ago = (7 + day_num - day_num_target) % 7
	if days_ago == 0:
		days_ago = 7
	target_date = start_date - timedelta(days=days_ago)
	return target_date
print(datetime.today())
print(get_previous_byday('Monday'))


# Suggest use another modul


from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d= datetime.now()
print(d)

# Next Friday
print(d+ relativedelta(weekday=FR))

# Last Friday
print(d+ relativedelta(weekday=FR(-1)))



#

'Finding the Date Range for the Current Month'


from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
	if start_date is None:
		start_date = date.today().replace(day=1)
	_, days_in_month = calendar.monthrange(start_date.year, start_date.month)
	end_date = start_date + timedelta(days=days_in_month)
	return (start_date, end_date)
a_day = timedelta(days=1)

first_day, last_day = get_month_range()
print(first_day, last_day)


# A date time loop
def date_range(start, stop, step):
	while start < stop:
		yield start
		start += step

for d in date_range(datetime(2014,11,11), datetime(2014,11,20), timedelta(hours=6) ):
	print(d)


'Converting Strings into Datetimes'

text= '2013-10-20'

y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
print(z-y)



# datetime.strptime() methods  %Y four-digt year %m two-digit month


print(z)
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)


'Manipulating Date involving Time Zones'


from datetime import datetime
from pytz import timezone

d= datetime(2012,12,21,9,30,0)
print(d)


# Localize the date for Chicago
central = timezone('US/Central') # assign some timezone
loc_d = central.localize(d)  # point it as local timezone.
print(loc_d)

# Convert to Bangalore time

bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))

print(bang_d)

print(dir(timezone))