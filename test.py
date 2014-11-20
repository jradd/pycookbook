

# 2013-10-9
# 2013/10/9
# 2013-9-10
# year = 2013
# month= 10
# day =9


import re
ex1 = "2013-10-9"

# \d :  0123456789
# \D

res = re.split('\D',ex1)
print(res)

def formatDate(date):
	if len(date) == 8 :
		year, month, day = date[:4], date[4:6], date[6:]
	else:
		year, month, day = re.split('\D',date)
	return year, month, day


print(formatDate('20141030'))
print(formatDate('2014-10-30'))
print(formatDate('2014/10/30'))


date = "2014-10-30"
print("Date: Year-%s, Month-%s, Day-%s" % (formatDate(date)))



