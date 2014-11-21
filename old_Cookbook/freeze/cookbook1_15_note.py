'1.15 Grouping Records Together based on a Field'

"""
Problem

You have a sequence of dictionaries or instances and you want to iterate over the data in groups based on the value of a particular field, such as date.


"""


rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]


# group by date,  ---  itertools.groupby

# to do it, first sort by the desired field ,  in this case, date

from operator import itemgetter
# rows.sort(key=itemgetter('date'))

# or use lambda
rows = sorted(rows, key=lambda val: val['date'])
from itertools import groupby

# Iterate in groups

for date, items in groupby(rows, key = itemgetter('date')):
	print(date)
	for i in items :
		print (i)

from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
	rows_by_date[row['date']].append(row)
print('-'*40)
print(rows_by_date)