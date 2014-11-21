'1.10 Removing Duplicates from a sequence while Maintaining Order'


'Removing Duplicates from a Sequences while maintaining order'
'if i(jinyong) want to kill duplicates in a list i will:'
a = [1,5,2,1,9,1,9,10]
print set(a) # the order will change from raw order.



'problem: want to eliminate the duplicate values in a  sequences but preserve the orde of remaining values'

def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

a = [1,5, 2, 1, 9, 1, 5, 10]
c = list(dedupe(a))
print c

'up: only works for the sequence are hashable'
'if unhashable types (like dicts)'

def dedupe(items, key = None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)


a = [{'x': 1, 'y':2}, {'x':1, 'y':3}, {'x': 1, 'y':2}, {'x':2,'y':4}]
c = list(dedupe(a, key = lambda d: (d['x'], d['y'])))
print c

d = list(dedupe(a, key = lambda d: d['x']))
print d


' if we want to remove duplicate lines in a file'

"""
with open(somefile,'r') as f:
	for line in dedupe(f):
		...
"""

