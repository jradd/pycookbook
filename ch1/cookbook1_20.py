'1.20 Combining Multiple Mapping into a SIngle Mapping'

'''
Problem

You have multiple dictionaries or mappings that you want to logically combine into a single mapping to perform certain operations, such as looking up values or checking for the existence of keys.
'''


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap

c = ChainMap(a, b)

print((c['x'])) # from a
print((c['y'])) # from b
print((c['z'])) # 3 from a, a ois first

d = ChainMap(b, a)
print((d['x'])) # from a
print((d['y'])) # from b
print((d['z'])) # 4 from b.  b is first
