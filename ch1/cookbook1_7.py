'1.7 Keeping Dictionaries in Order'

'''
Problem

You want to create a dictionary, and you also want to control the order of items when iterating or serializing.
'''

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print(d)
#>> OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])


import json
print(json.dumps(d))
# >>{"foo": 1, "bar": 2, "spam": 3, "grok": 4}