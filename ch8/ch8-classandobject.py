'8.1 Changing the String Representation of Instances'

'''Problem

You want to change the output produced by printing or viewing instances to something more sensible.'''
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __repr__(self):
        return 'A Point({self._x!r}, {self._y!r})'.format(self=self)
    def __str__(self):
        return '(Point::{self._x!r}, {self._y!r})'.format(self=self)

p = Point(3, 4)
print(p) ##  str
print(repr(p))


# Discussion

'''

Defining __repr__() and __str__() is often good practice, as it can simplify debugging and instance output. For example, by merely printing or logging an instance, a programmer will be shown more useful information about the instance contents.
'''




'8.2 Customizing String Formatting'

_formats = {
	'ymd': '{d.year}-{d.month}-{d.day}',
	'mdy': '{d.month}/{d.day}/{d.year}',
	'dmy': '{d.day}/{d.month}/{d.year}',
	'yymmdd': '{d.year:2d}{d.month:02d}{d.day:02d}',
	'yyyymmdd':'{d.year}{d.month:02d}{d.day:02d}'
}

class Date:
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
	def __format__(self, code='ymd'):
		if code == '':
			code = 'ymd'
		if code == 'yymmdd':
			return _formats[code].format(d= Date(int(str(self.year)[-2:]), self.month, self.day))
		fmt = _formats[code]
		return fmt.format(d=self)

d = Date(2014, 7, 5)
print(format(d))
print(format(d,'mdy'))
print(format(d,'dmy'))
print(format(d,'yyyymmdd'))
print(format(d,'yymmdd'))
print('{0:02d}'.format(3))



'Or you better use the default format of datetime'

from datetime import date
d = date(2012,3,4)
print(format(d))
print(format(d, '%A, %B, %d, %Y')) # A weekday, B month
print(format(d, '%d, %B, %Y'))


'''
'Making Objects Support the Context-Management Protocol'

'problem: You want to make your objects support the context-management protocol (the with statement).'''



from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
	def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
		self.address = address
		self.family = AF_INET
		self.type = SOCK_STREAM
		self.sock = None
	def __enter__(self):
		if self.sock is not None:
			raise RuntimeError('Already connected')
		self.sock = socket(self.family, self.type)
		self.sock.connect(self.address)
		return self.sock

	def __exit__(self, exc_ty, exc_val, tb):
		self.sock.close()
		self.sock = None


from functools import partial

conn = LazyConnection(('www.python.org', 80))
# Connection closed
# with conn as s:
#     # conn.__enter__() executes: connection open
#     s.send(b'GET /index.html HTTP/1.0\r\n')
#     s.send(b'Host: www.python.org\r\n')
#     s.send(b'\r\n')
#     resp = b''.join(iter(partial(s.recv, 8192), b''))
#     print(resp)
#     # conn.__exit__() executes: connection closed

# When the with statement is first encountered, the __enter__() method is triggered



'8.4 Saving Memory When Creating a Large Number of Instances'

'p: Your program creates a large number (e.g., millions) of instances and uses a large amount of memory.'

class Date:
	__slots__ = ['year', 'month','day']
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day


'8.5 Encapsulating Names in a Class'

class A:
    def __init__(self):
        self._internal = 0    # An internal attribute
        self.public = 1       # A public attribute

    def public_method(self):
        '''
        A public method
        '''


    def _internal_method(self):
        'A internal method'


class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        ...
    def public_method(self):
        'public'


'Creating Managed Attributes'
class Person:
	def __init__(self, first_name):
		self.first_name = first_name
	# Getter function
	@property
	def first_name(self):
		return self._first_name
	#Setter function
	@first_name.setter
	def first_name(self, value):
		if not isinstance(value, str):
			raise TypeError('Expected a string!')
		self._first_name = value

	# Deleter function (optional)
	@first_name.deleter
	def first_name(self):
		raise AttributeError("Can't delete attribute")


'''
It’s important to stress that the @first_name.setter and @first_name.deleter decorators won’t be defined unless first_name was already established as a property using @property.
'''


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4)
print(c.radius)

# those two function need not to ( ) cauz they are properties too.
print(c.area)
print(c.perimeter)


'Calling a Method on a Parent Class'