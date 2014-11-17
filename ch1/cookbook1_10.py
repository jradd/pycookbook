
'1.10 Removing duplicates maintaing order'

"""
Problem

You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items.


"""

# case1 values are hashable

def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

items = [1,2,3,4,5,4,3,2]
print(list(dedupe(items)))
# [1, 2, 3, 4, 5]


# case 2 values are not hashable

def dedupe(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print(list(dedupe(a, key=lambda d: (d['x']))))
#>> [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
#>> [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]