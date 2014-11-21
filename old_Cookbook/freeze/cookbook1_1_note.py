## -*- coding: utf-8 -*-

__author__ = 'STEVE'
'Python Cookbook edi.3'
'Chapter 1 Data Structures and Algorithms'

""">>>
	`````Python provides a variety of useful built-in data structures, such as lists, sets, and dictionaries. For the most part, the use of these structures is straightforward. However, common questions concerning searching, sorting, ordering, and filtering often arise. Thus, the goal of this chapter is to discuss common data structures and algorithms involving data. In addition, treatment is given to the various data structures contained in the collections module.
"""

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


"""
i began to learn python in October 2014.
	Started from python cookbook, i will finish this book , as soon. Today, 11-08-2014 "

"""

"1.1 Unpacking a Sequence into Separate Variable"


"***********************************************************"
p = (4,5)
x, y = p
print 'x= %s, y=%s' %(x,y) # x=4,y=5

data = ["AAPLE", 50, 100, (2012,12,21)]
name, share, price , date = data
print date # (2012,12,21)
name, share, price, (year, mon, day) = data
print 'date: %s-%s-%s' %(year,mon,day) # date: 2012-12-21

'If there is a mismatch in the number of elements, you"ll get an error'
try:
	x, y, z = (43,3)
except ValueError:
	print ValueError("need match values to unpack")


#ValueError: need more than 2 values to unpack



'above, we can unpack tuples, lists, what about other types of data'
a,b,c,d,e = 'Hello'  # String like list, so here we can see it faster.


'When unpacking, maybe i need descard certain values. '

data = ['ACME', 50, 91.1, (2012,12,21)]
_, shares, price, _ = data
print shares  # just keep shares and prices
_, month, _ = date
print month