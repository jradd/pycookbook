'Chapter 2 Strings and Text'

'2.1 Splitting Strings on Any of Multiple Delimiters'
"""
Problem

You need to split a string into fields, but the delimiters (and spacing around them) aren’t consistent throughout the string.
"""
line = 'asdf fjdk; afed, fjek,asdf,     foo'

import re
# better than split()
print(re.split(r'[;,\s]\s*', line))
# delimiters are note import, just want to remove them.
#>> ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


# want to keep delimiters???
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
#>> ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']


# split characters useful?
# use double slice to separate values and delimiters.
values = fields[::2]
delimiters = fields[1::2] + [""]

print(values)
print(delimiters)

a = ''.join(v+d for v, d in zip(values, delimiters))
print(a)
b = re.split(r'(?:,|;|\s)\s*',	line)
print(b)