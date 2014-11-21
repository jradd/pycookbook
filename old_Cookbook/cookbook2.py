#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'STEVE'

"""documents:
cookebook - 2
"""

' string and text'

"***********************************************************"

'2.1 splitting  on any of multiple delimiters'

As = 'test test test ; test, test . '
import re
print re.split(r'[\s;,.]', As)


'正则模式 ? 开头 表示意思 '



'2.2 Match String at the start or end'

'startswith  endswith'

# a coenvient way to perform basic prefix and suffix checking .
# 文件扩展名   网页地址前缀.

string = 'spam.txt'
print string.startswith('s')
print string.endswith('txt')


'2.3 Using Shell wildcard Patterns'

from fnmatch import fnmatch, fnmatchcase
print fnmatch('foo.txt', '*.txt')
names = ['Dat3.csv', 'Dat4.csv', 'afda.txt'
]
print [name for name in names if fnmatch(name, 'Dat*.csv')]



'2.4 Matching and Searching for text Patterns '

text = 'yeah, but no, but yeah, but no, but yeah'

print text.find('no')

text1 = '11/27/2013'
text2= '01/02/2014'
test3 = 'Nov 2, 2012'
import re
# if re.match()

text = "Today is 11/27/2012, Pycon starts 3/13/2013"
datepat = re.compile(r'\d+/\d+/\d+')

print datepat.findall(text)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print datepat.findall(text)


for month, day, year in datepat.findall(text):
	print ('{}-{}-{}'.format(year, month, day))



'2.5 Searching and Replacing Text'

