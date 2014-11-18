'1.9 Transfoming and Reducing Data at the Same Time'

'''
Problem

You need to execute a reduction function (e.g., sum(), min(), max()), but first need to transform or filter the data.
'''


nums = list(range(1,6))

s = sum( x * x for x in nums)

print(s)

import os
files = os.listdir('.')
# print files

if any(name.endswith('.py')  for name in files ):
	print ('There be python!')
else:
	print ('Sorry, no python files')


# output a tuple as csv

s = ('ACME', 50, 123.45)
print (','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
	{'name':'GOOG', 'shares':50},
	{'name':'YHOO', 'shares':75},
	{'name':'AOL', 'shares':20},
	{'name':'SCOX', 'shares':65},
]

min_shares = min(s['shares'] for s in portfolio)

print(min_shares)

#
min_shares = min(portfolio, key = lambda s : s['shares'])
print(min_shares)