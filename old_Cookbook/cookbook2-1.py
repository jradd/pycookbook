'Chapter 2 Strings and Text'

'2.1 Splitting Strings on Any of Multiple Delimiters'
"""
Problem

You need to split a string into fields, but the delimiters (and spacing around them) aren’t consistent throughout the string.
"""
line = 'asdf fjdk; afed, fjek,asdf,     foo'

import re

# better than split()
print re.split(r'[;,\s]\s*', line)


fields = re.split(r'(;|,|\s)\s*', line)
print fields

# split characters useful?

values = fields[::2]

delimiters = fields[1::2] + [""]

print values
print delimiters

print ''.join(v+d for v, d in zip(values, delimiters))

print re.split(r'(?:,|;|\s)\s*',	line)
