'Chapter 4 Generator'


'4.x Defining Generator Functions with Extra State'



from collections import deque
class linehistotry:
	def __init__(self, lines, histlen=3):
		self.lines = lines
		self.history= deque(maxlen = histlen)
	def __iter__(self):
		for lineno, line in enumerate(self.lines, 1):
			self.history.append( (lineno, line))
			yield line

	def clear(self):
		self.history.clear()

somefile ="""
Newyourk,
Olmda
ITGONG
LUN
::
"""

lines = linehistotry(somefile)
for line in lines:
	if 'O' in lines:
		for lineno, hline in lines.history:
			print('{}:{}'.format(lineno, hline), end='')



'Taking a Slice of an Iterator'

def count(n):
	while True :
		yield n
		n +=1

c = count(0)
# TypeError: 'generator' object is not subscriptable
# c[10:20] # error
import itertools
for x in itertools.islice(c, 10 , 20):
	print(x)


'Skipping the First Part of an Iterator'

# with open('cookbook.py',encoding='utf-8') as f:
# 	for line in f:
# 		print(line,end=' ')

# Want to skip this line: # .... # ...

# from itertools import dropwhile
# with open('cookbook.py',encoding='utf-8') as f:
# 	for line in dropwhile(lambda line: line.startswith('#') , f):
# 		print(line, end='')



'Permutation'

items = ['a','b','c']
from itertools import permutations
for p in permutations(items):
	print(p)

for p in permutations(items,2):
	print(p)

# combination.

from itertools import combinations
for c in combinations(items,3):
	print(c)

for c in combinations(items,2):
	print(c)

for c in combinations(items,1):
	print(c[0]) # c like  ('a',)

# with replacement
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
	print(c)


'Iterate with Index'
# default index, starts with 0
for idx, val in enumerate(items):
	print(idx, val)

# You can modify the default start index , like this
for idx, val in enumerate(items,10):
	print(idx, val)

'Iterating over multiple sequences simultaneously'

xpts = [1,5,4,2,10,7]
ypts = [101,78,37,15,62,99,100]

for x,y in zip(xpts, ypts):
	print(x,y)

# zip() works , produces tuple(x,y)

# remind: y have 7 values, while x have 6values
# defaultmode of zip,  get smaller.
xpts = [1,5,4,2,10,7]
ypts = [101,78,37,15,62,99,100]

print('zip have longest ')
from itertools import zip_longest
for i in zip_longest(xpts, ypts):
	print(i)
# None, 100  have added.

for i in zip_longest(xpts, ypts, fillvalue= 'Missing'
                  	):
	print(i)

'how about three list, simultaneously'

a = [1,2,3]; b=[10,11,12]; c=['alpha','beta','gamam']

for i in zip(a,b,c):print(i)



'Iterating on items in separate containers'

from itertools import chain
for x in chain(a, c):print(x)

# chain link two list.

a = [1,2,3]; b=set(['a','b','c'])
print(a);
print(b)
for x in chain(a,b):print(x) # chain done, but order change.


# itertools.chain() accepts one or more iterables as arguments.

'Flatten Nested Sequence'

a = [12,[12,[1,[2,3]]]]

print(a)
print('flatten')

from collections import Iterable

def flatten(items, ignore_types = (str, bytes)):
	for x in items:
		if isinstance(x, Iterable) and not isinstance(x, ignore_types):
			yield from flatten(x)
		else:
			yield x

items = [1,2, [3,4,[5,6], 7], 9]
for x in flatten(items):print(x)