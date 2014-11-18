'1.8  Mapping Names to Sequence Elements '

"""Problem
You have code that accesses list or tuple elements by position, but this makes the code somewhat difficult to read at times. You’d also like to be less dependent on position in the structure, by accessing the elements by name.

use namedtuple
"""

from collections import namedtuple

subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# so Subscriber - this tuple's name, and [0] = ['addr'] [1] = [joined]
sub = subscriber('jonesy@example.com', '2012-10-19')

print(sub)

print(sub.addr)
print(sub.joined)


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# use ,  convert a dict to a namedtuple
stock_prototype = Stock('',0, 0.0, None,None)
def ditc2stock(s):
	return stock_prototype._replace(**s)

a = {'name':'acme','shares':100, 'price':45, 'date':None, 'time':None}
print(ditc2stock(a))
a = {'name':'acme','shares':100 }

print(ditc2stock(a))

