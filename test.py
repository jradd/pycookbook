#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = ""

import re
text = 'today is not 2014-10-20'
datepatt = re.compile(r'\d{4}-\d{2}-\d{2}')
print(datepatt.findall(text))
#>> ['2014-10-20']

text2 = 'today is not 2014-10-20, and not 2014-11-20'
print(datepatt.findall(text2))
#>> ['2014-10-20', '2014-11-20']


datepatt2 = re.compile(r'\d{4}-?\d{2}-?\d{2}')
text = 'today is not 2014-10-20, and not 2014-11-20. LOL just a exaple 20140101'
print(datepatt2.findall(text))
#>> ['2014-10-20', '2014-11-20', '20140101']


datepatt3 = re.compile(r'\d{4}[-/]?\d{2}[-/]?\d{2}')
text = 'today is not2014-10-20, and not 2014-11-20. LOL just a exaple 20140101  sdjfkl2014/02/03'
print(datepatt3.findall(text))
#>> ['2014-10-20', '2014-11-20', '20140101', '2014/02/03']



datepatt4 = re.compile(r'\d{2,4}[-/]?\d{2}[-/]?\d{2}')
text = 'today is not2014-10-20, and not 2014-11-20. LOL just a exaple 20140101  sdjfkl2014/02/03 140204   www.14-02-05'
print(datepatt4.findall(text))



datepatt5 = re.compile(r'(\d{2,4})[-/]?(\d{2})[-/]?(\d{2})')
text = 'today is not 20141020, and not 2014/11/20. LOL just a exaple 20140101  142024'

print(datepatt5.sub(r'\1-\2-\3', text))


datein1 = '20141020'
# print(datepatt5.match(datein1))
m = datepatt5.match(datein1)
print(m.group()) # 20141020 .group() 就会返回能匹配的整体
print(m.groups()) # groups() 会把各个组单独匹配到的结果 合并起来成为一个集合 如下行所示
#>> ('2014', '10', '20')
# 既然是集合, 就可以序号来访问了  不过访问是换成 group(序号)
print(m.group(1)) # 2014
print(m.group(2)) # 10
print(m.group(3)) # 20
try:
	print(m.group(4))
except:
	pass
print(m.groups()) # ('2014', '10', '20')
# print(dir(m))
#>><_sre.SRE_Match object; span=(0, 8), match='20141020'>

#>> today is not 2014-10-20, and not 2014-11-20. LOL just a exaple 2014-01-01  14-20-24

# print(datepatt4.findall(text))




patt1 = re.compile(r'(\d+)[-/](\d+)[-/](\d+)')
patt2 = re.compile(r'(\d+)[-/](\d+)[-/](\d+)')

# print(patt1.match(text))
# <_sre.SRE_Match object; span=(0, 10), match='2014-10-20'>




# # 2013-10-9
# # 2013/10/9
# # 2013-9-10
# # year = 2013
# # month= 10
# # day =9


# import re
# ex1 = "2013-10-9"

# # \d :  0123456789
# # \D

# res = re.split('\D',ex1)
# print(res)

# def formatDate(date):
# 	if len(date) == 8 :
# 		year, month, day = date[:4], date[4:6], date[6:]
# 	else:
# 		year, month, day = re.split('\D',date)
# 	return year, month, day


# print(formatDate('20141030'))
# print(formatDate('2014-10-30'))
# print(formatDate('2014/10/30'))


# date = "2014-10-30"
# print("Date: Year-%s, Month-%s, Day-%s" % (formatDate(date)))
# from unicode import unicode
# string = '天下第一剑'
# for s in string:
# 	print(unicode(s))



qqpattern = re.compile(r'\d+@qq.com')
text = '1231@qq.com 123123qq.com 321@qq.com.cn 123@qq.cn'
print(qqpattern.findall(text))



'translate'

s = 'asdfa123adsfawqr'
print(s.translate('aeiuo'))