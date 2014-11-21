'Chapter 6 Data Encoding and Processing'


import csv

"""
	The main focus of this chapter is using Python to process data presented in different kinds of common encodings, such as CSV files, JSON, XML, and binary packed records. Unlike the chapter on data structures, this chapter is not focused on specific algorithms, but instead on the problem of getting data in and out of a program.
"""

'6.1 Reading and Writing CSV Data'


file = 'test.csv'


with open(file) as f:
	f_csv = csv.reader(f)
	headers = next(f_csv)
	print("header",headers)
	for row in f_csv:
		print(row)
# access some certain fields, you will use index, such as
# row[0] (Stock Symbol)  row[4] (Change)

# use Chapter 1 -- namedtuple  make it convenient.


# use namedtuple instead of indexing
from collections import namedtuple
header=['sym','bol']
testNamedTuple=namedtuple('test', header)
mtest = testNamedTuple("AAA", "BBB")
print(mtest) # test(sym='AAA', bol='BBB')

with open(file) as f:
	f_csv = csv.reader(f)
	headings = next(f_csv)
	Row = namedtuple('Row', headings)
	print(Row)
	for r in f_csv:
		row = Row(*r)
		print("Symbol", row.Symbol, "\t", "Price",row.Price)

# This would allow you to use the column headers such as row.Symbol and row.Change instead of indices.




# Another reader method : DictReader
# In this version, you would access the elements of each row using the row headers. For example, row['Symbol'] or row['Change'].
print("use DictReader instance")
with open(file) as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		print("\tSymbol:", row["Symbol"], "\t\tPrice:", row["Price"])

import csv
from pprint import pprint
from collections import OrderedDict
with open(file) as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		pprint(row)
		# You will find the order is changed (not the header order)
		# Keep the specified order? think about OrderedDict


##### Csv Writer

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
        # write a new stock of my own
        ('HANG',9999,'03/01/2013','1:51pm','+14',100000)
       ]
# write mode1:    normal writer
with open('mystocks_normal_way.csv','w') as f:
	f_csv = csv.writer(f)
	f_csv.writerow(headers)
	# Each row is a tuple, so write rows can write row-list
	f_csv.writerows(rows)
	print('write done!')

# write mode2 :  Dcitwriter
#headers is same as preceding.
# Differently  row list is a list of dicts.
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]

with open('mystocks_dict_way.csv', 'w') as f:
	f_csv = csv.DictWriter(f, headers)
	f_csv.writeheader()
	# write list of di
	f_csv.writerows(rows)


# about TSV ( tab - sepate)

# Example of reading tab-separated values
# with open('stock.tsv') as f:
#     f_tsv = csv.reader(f, delimiter='\t')
#     for row in f_tsv:
#         # Process row
#         ...




"Want set specified type of data"

col_types = [str, float, str, str, float, int]
with open('test.csv', 'r') as f:
	f_csv = csv.reader(f)
	headers= next(f_csv)
	for row in f_csv:
		# Apply conversions to the row items
		row = tuple(convert(value) for convert, value in zip(col_types, row))
		print(row)
