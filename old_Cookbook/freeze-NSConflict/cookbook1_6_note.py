'1.6 Mapping Keys to Multiple Values in a Dictionary'

'''
Problem

You want to make a dictionary that maps keys to more than one value (a so-called "multidict").

'''

d = {'a' : [1,2,3],
	'b':[4,5]}

print(d)
#>> {'a': [1, 2, 3], 'b': [4, 5]}

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)
d['a'].append(4)
d['b'].append(2)
print(d)
#>> defaultdict(<class 'list'>, {'a': [1, 2, 4, 4], 'b': [2]})
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(4)
d['a'].add(4)
d['b'].add(2)
print(d)
#>> defaultdict(<class 'set'>, {'a': {1, 2, 4}, 'b': {2}})
d = {}

d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('a', []).append(4)
d.setdefault('b', []).append('z')
d.setdefault('b', []).append('c')

print(d)# regular dictionary
#>> {'b': ['z', 'c'], 'a': [1, 2, 4]}
