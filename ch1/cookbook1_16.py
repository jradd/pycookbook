'1.16 Filtering Sequence Elements'

"""
Problem

You have data inside of a sequence, and need to extract values or reduce the sequence using some criteria.

"""
"Comment mainly use List Comprehension"


import random
mylist = [random.randint(10, 20) for i in range(10)]

print([n for n in mylist if n > 14])


values = ['1','2','3','4', '-','N/A']


# or use filter function ( define a function that return boolean type to filter)
def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

ivals = list(filter(is_int, values))

print(ivals)


' compress'

from itertools import compress
print(list( compress([1,2], [True,False])))
# compress is like a selection-vector,  choose the "True" position.



addresses = ['5412 N CLARK', '5148 N CLARK', '5800 E 58TH', '2122 N CLARK', '5645 N RAVENSWOOD', '1060 W ADDISON', '4801 N BROADWAY', '1039 W GRANVILLE']
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n>5 for n in counts]
print(more5)
print(list(compress(addresses, more5 )))



"""
 filter(), compress() normally returns an iterator. Thus, you need to use list() to turn the results into a list if desired.
"""