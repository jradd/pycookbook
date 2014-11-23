'ch7 '


'7.1 Functions that accept any number of arguments'

def avg(first, *rest):
	return (first + sum(rest)) / (1+ len(rest))

# Sample use
print(avg(1,2))
print(avg(1))
print(avg(1,2,3,4))

# rest is a tuple of all the extra positional arguments passed

'keyword arguments'
#
#To accept any number of keyword arguments, use an argument that starts with **
import html
def make_element(name, value, **attrs):
	keyvals = ['%s=%s' % item for item in attrs.items()]
	attr_str = ' '.join(keyvals)
	element = '<{name} {attrs}>{value}</{name}>'.format(name= name, attrs=attr_str, value = html.escape(value))
	return element

# example
# creates <item size="large" quantity="6">Albatross</item>
print(make_element('item','Albatross',size="large",quantity=6))



def anyargs(*args, **kwargs):
	print(args)
	print(kwargs)
anyargs(1,2,3,key=3,must=4)


'7.2 Writing Functions that only take keyword arguments'

def recv(maxsize, *, block):
	'Receives a message'
	print('recv calling')
	pass

# print(recv(1024, True)) # TypeError
print(recv(1024,block=True))


def minimum(*values, clip=None):
	m = min(values)
	if clip is not None:
		m = clip if clip > m else m
	return m
print(minimum(1,4,2,-5, 10))
print(minimum(1,4,2,-5, 10, clip = 0))


"""
Keyword-only arguments are often a good way to enforce greater code clarity when specifying optional function arguments. For example, consider a call like this:
"""

print(help(recv))
print(help(minimum))


'7.3 Attaching Informational Metadata to Function Arguments'

# def add(x:int, y:int) -> int:
# 	add two int, return a int'
# 	return x+y
# print(add(3,5))
# print(help(add))
# print(add.__annotations__)

'7.4 Returning Multiple Values from a Function'
def myfun():
	return 3,2,1
a,b,c = myfun()
print(a,b,c)


'7.5 Defining Functions with Default Arguments'

def spam(a, b=42):
	return (a,b)
print(spam(4))
print(spam(4,32))

def spam(a, b=None):
	if b is None:
		b = []
	# b = tuple(?b)
	return (a,b)
print(spam(3,4))

_no_value = object()
def spam(a, b = _no_value):
	if b is _no_value:
		print("No b value supplied")


def spam(a, b = []):
	pass

'7.6 Defining Anonymous or Inline Functions'

add = lambda x, y: x+y
print(add(2, 3))
print(add('heelo',' world'))

names = ['David Beazley','Brian Joines','Raymond Hettinger',' Ned Batchelder']
sorted_names = sorted(names, key =lambda name: name.split()[-1].lower())

print(sorted_names)


'7.7 Capturing Variables in Anonymous Function'
x = 10
a = lambda y: x+y
x = 20
b = lambda y: x+y
print(a) # <function <lambda> at 0x102391158>
print(b) # <function <lambda> at 0x1023911e0>
print(dir(a))
print(a.__annotations__)
print(a.__repr__)
print(a(10), b(10))


'7.8 Making an N-Argument Callable Work as a Callable with Fewer Arguments'


def spam(a,b,c,d):
	print(a,b,c,d)

# partial

from itertools import partial
