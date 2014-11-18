#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = ""

'2.9 Normalizing Unicode Text to a Standard Representation'
"""Problem

You’re working with Unicode strings, but need to make sure that all of the strings have the same underlying representation.
"""

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print((s1).encode('utf-8'))
print(s2) # UnicodeEncodeError: 'gbk' codec can't encode character '\u0303' in position


import unicodedata

t1 = unicodedata.normalize('NFC', unicode(s1))
t2 = unicodedata.normalize('NFC', unicode(s2))

print(t1, t2)
print(s1 == s2,  t1==t2)


'2.10 Working with Unicode Character in Regular Expressions'

import re
num = re.compile('\d+')

# ASCII digits
print(num.findall('123'))


# Arabic digits
print(num.findall('\u0661\u0662\u0663'))


arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]]+')

pat = re.compile('stra\u00dfe', re.I)
s = 'straße'
print(pat.findall(s))