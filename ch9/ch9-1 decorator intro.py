'ch9 MetaProgramming'

'DRY rule -- Donot repeat yourself!!!!'


'''Problem
You want to put a wrapper layer around a function that adds extra processing (e.g., logging, timing, etc.).
'''

# need to wrap a function with extra code, define a decorator

import time
from functools import wraps

def timethis(func):
	'''
	Decorator that reports the execution time.
	'''
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__, end-start)
		return result
	return wrapper

# example of using the decorator

@timethis
def countdown(n):
	'''
	Counts down
	'''
	while n > 0:
		n-= 1

(countdown(100000))
(countdown(100))


'A decorator is a function that accepts a function as input and returns a new function as output. Whenever you write code like this:'

'之前的装饰效果类似于:'

# def countdown(n):
#     ...
# countdown = timethis(countdown)


'Are there any buit-in decorators???'
'@staticmethod'
'@classmethod'
'@property'

'下面是例子'


class A:
	@classmethod
	def method(cls):
		print('its a class method call. ')


a = A()
a2 = A()
a.method(); a2.method()

class B:
	# Equivalent definition of a class method
	def method(cls):
		print('its a class method call.  class: B')
	method = classmethod(method)

b = B()
b2 = B()
b.method(); b2.method()

