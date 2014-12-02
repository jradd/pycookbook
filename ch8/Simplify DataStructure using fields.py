'Simplifying the initialization of Data Structures'

'http://is.gd/PEJTs2'

import math
class Structure:
	# Class Variable that specifies expected fields
	_fields=[] # like a namespace
	def __init__(self, *args):
		if len(args) != len(self._fields):
			raise TypeError("Expected {} arguments".format(len(self._fields)))

		# Set the arguments
		for name, value in zip(self._fields, args):
			setattr(self, name, value)


#2 support keyword arguments!

class Structure:
	# Class Variable that specifies expected fields
	_fields=[] # like a namespace
	def __init__(self, *args, **kwargs):
		if len(args) > len(self._fields):
			raise TypeError("Expected {} arguments".format(len(self._fields)))

		# Set all of the positional arguments
		for name, value in zip(self._fields, args):
			setattr(self, name, value)
		# Set the remaining keyword arguments
		for name in self._fields[len(args):]:
			setattr(self, name, kwargs.pop(name))
		if kwargs:
			raise TypeError('Invalid arguments')

# Example class definitions
if __name__ == '__main__':
	class Stock(Structure):
		_fields = ['name','shares','price']

	class Point(Structure):
		_fields = ['x','y']
	class Circle(Structure):
		_fields = ['radius']
		def area(self):
			return math.pi * self.radius **2


	s = Stock('ACME', 50, 91.1)
	p = Point(2,3)
	c = Circle(3)
	s2 = Stock('GooG',50,price=100)