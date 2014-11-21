'Chapter 4. Iterators and Generators'


'4.1 Manually Consuming an Iterator'

'''
	Problem
		need to process item in an iterable, but do not use for loop
'''


items = [1, 2, 3]
# get the iterator
it = iter(items)

# Run the iterator
print next(it)
print next(it)
print next(it)

# StopIteration
# print next(it)