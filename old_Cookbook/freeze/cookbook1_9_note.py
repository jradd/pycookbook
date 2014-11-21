'1.9 Finding Commonalities in Two Dicts'
"""
Problem

You have two dictionaries and want to find out what they might have in common (same keys, same values, etc.).
"""

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}


# Find keys in common
'Python 3 supported'

print(a.keys() & b.keys())
#>> {'y', 'x'}
print(a.keys() - b.keys())
#>> {'z'}

# Find (key, value) in common
print(a.items() & b.items())
#>> {('y', 2)}
