## -*- coding: utf-8 -*-

__author__ = 'STEVE'

import sys
from collections import deque # 1.3
import heapq # 1.4
from collections import defaultdict # 1.6
from collections import OrderedDict # 1.7
import json # 1.7
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


"something i learning from python cookbook"

"1.1"
"***********************************************************"
p = (4,5)
name, share, price , date = ["AAPLE", 50, 100, (2012,12,21)]
print date
#x, y, z = (43,3)
#ValueError: need more than 2 values to unpack

# or you can just get key information
_, month, _ = date
print month
"***********************************************************"
"1.2"
# Python 3.3

# def drop_first_last(grades):
# 	first, *middle, last = grades
# 	return avg(middle)
# print drop_first_last([1,2,3,4])

"***********************************************************"
"1.3 deque"
def search(lines, pattern, history):
	previouse_lines = deque(maxlen = history)
	for line in lines:
		if pattern in line:
			yield line , previouse_lines
		previouse_lines.append(line)


m = [1,2,3,4,5]
n = deque(maxlen=3)
print n
n.append(1)
n.append(2)
n.append(3)
print n
n.append(4)
print n

"***********************************************************"
"1.4"
nums = [1,8,2,23,7,-4,18,23,42,37,2]
print (heapq.nlargest(3, nums))
# [42,37, 23]
print (heapq.nsmallest(3, nums))
# [-4, 1, 2]

porfolio = [
			{"name":"IBM", "shares": 100, "price":91.1},
			{"name":"Apace", "shares": 100, "price":11.1},
			{"name":"GOOGL", "shares": 100, "price":21.1},
			{"name":"MSFT", "shares": 100, "price":31.1},
			{"name":"HPQ", "shares": 100, "price":41.1},
			]
cheap =  heapq.nsmallest(3, porfolio, key = lambda s: s["price"])
expensive = heapq.nlargest(3, porfolio, key = lambda s: s["price"])

print cheap
print expensive

heap = list(nums)
print heap
heapq.heapify(heap)
print heap # heap[0] is always the smallest item.

"***********************************************************"
"1.5 Implementing a Priority Quene"

class PriorityQuene:
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]

class Item:
	def __init__(self, name):
		self.name = name

	def _repr_(self):
		return 'Item ({!r})'.format(self.name)

q = PriorityQuene()
q.push(Item("foo"),1)
q.push(Item("bar"),5)
q.push(Item("pam"),3)
q.push(Item("grok"),1)
print q.pop()._repr_()
print q.pop()._repr_()
print q

"""about heappush heappop
>>> h = []
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')
"""

"***********************************************************"
"1.6 Mapping Keys to Multiple Values" # 多值字典
mm = {4,5}
print type(mm) # <type 'set'>
d = {'a':[1,2,3], 'b':[4,5]}
e = {'a':{1,2,3}, 'b':{4,5}}

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
for k, v in d.items():
	print k, '\t', v

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
for k, v in d.items():
	print k, '\t', v

# d[]

"""why use defaultdict
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> list(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
"""

"***********************************************************"
"1.7 keeping dictionaries in Order"

d = OrderedDict()
d['foo'] = 1
d['boo'] = 2
d['moo'] = 3
d['noo'] = 5
d['qoo'] = 4

for k in d:
	print (k, d[k])

print json.dumps(d)

"***********************************************************"
"1.8 Calculating with Dictionaries"
prices = {"ME":123, "BBB":456, "CC123C":78, "sdf_":4564}
min_prices = min(zip(prices.values(), prices.keys()))
max_prices = max(zip(prices.values(), prices.keys()))
print min_prices  # return tuple ( min_price, min_price_o_stock)

print max_prices

"sort the dict"
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print prices_sorted

# zip 做出来的对象只能使一次 如果调用统计 要再次zip
# 如下例

prices_and_names = (zip(prices.values(), prices.keys()))
print "min", min(prices_and_names)
print "max", max(prices_and_names)
# 为啥这里没有报错？  书上说出 valueError： max（）
# arg is an Empty sequence

print min(prices)
print max(prices)
# 按字典中key 值 长度排序、
print sorted(prices, key = lambda k : len(k))

"***********************************************************"
# "1.9 Finding Commonalities in Two Dictionaries"
# a = {'x':1, 'y':2, 'z':3}
# b = {'w':10, 'y':2, 'z':20}

# # Find key in common
# ak = a.keys()
# bk = b.keys()
# print a + k
# print a - k

# "目测需要Python 33支持。"

"***********************************************************"
