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



class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r}'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def dept_first(self):
        yield self
        for c in self:
            yield from c.dept_first()


root = Node('root')
child1 = Node('child1')
child2 = Node('child2')

root.add_child(child1)
root.add_child(child2)

child1.add_child(Node('child3'))
child1.add_child(Node('child4'))
child2.add_child(Node('child5'))

for ch in root.depth_first():
    print ch