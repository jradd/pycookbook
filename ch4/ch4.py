'Ch4 Iterators and Generators'


'4.1 Manually Consuming an Iterator'
import os

# maybe the following loop (next) is not suggested...
# with open('/Users/staticor/mygit/pycookbook/README.md') as f:
# 	try:
# 		while True:
# 			line = next(f)
# 			print(line, end=',')
# 	except StopIteration:
# 		pass

with open('/Users/staticor/mygit/pycookbook/README.md') as f:
	while True:
		line = next(f, None)
		if line is None:
			break
		print(line, end='')


'Delegating Iteration'

# define a __iter__

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
