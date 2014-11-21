#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = ""

'Chapter 3  Numbers, Dates and Times'

"****************************************************************************"

'3.1 Rounding'

print(round(1.23, 2) )
# print round(1.23, -1)
print(round(1.23, 1) )
print(round(12345678, -1))
print(round(12345678, -2))


x = 1.23456
print('value is {:0.3f}'.format(x))
a = 2.1; b = 4.3
print(a+b)
print(a+b == 6.4) # True in Py2
# in Python 3 it would be 6.300000000001



'3.2 Performing Accurate Decimal Calculate'


# Problem
# You need to perform accurate calculations with decimal numbers, and don’t want the small errors that naturally occur with floats.

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
ch = '3.3 Formatting Numbers'
print(ch)
# x = 1234.56789
# print format(x, '0.2f')
# # right justified
# print format(x, '>10.1f')
# print format(x, '<10.1f')
# print format(x, '^10.1f')

# # inclusion of thousands separator
# print format(x, ',')

# # Sci

# print format(x, 'e')


ch = '3.4 Work with Binary, Octal and Hexadecimal'
print(ch)

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

# format
print(format(x, 'b'))
print(format(x, 'o')) # no 0
print(format(x, 'x')) # no 0x
print(int('4d2', 16))
print(int('100001000', base = 2) )

# if __name__ == '__main__':main()


ch = '3.5 Packing and Unpacking Large integers fom bytes'


data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print(data)
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))
print(523**823)


ch = '3.6 Performing Complext - Valued Math'
# Def:
a = complex(3, 4)
b = 3 - 5j
print(a)
print(b)
# attr
print(a.real)
print(a*b)
print(abs(a))
# sines, cosines, or square roots, use the cmath module
import cmath
print(cmath.sin(a))




ch = '3.7 Work with Inf and NaNs'
# def
a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(type(a))
print(a*b)
print(a*c)
import math
# is function
print(math.isinf(a))
print(math.isnan(c))
d = float('nan')
print(c==d) # False
print(c is d) # False


ch = '3.8 Calculate with Fractions'

from fractions import Fraction
# Def
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a+b)
print(a*b)

# ATTR
print(a.numerator) # fenzi
print(b.denominator) # fenmu

# Convert
print(float(a))
c = Fraction(35,64)
print(float(c))
print(c.limit_denominator(12))

# Convert

x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)

ch = '3.9 Calculate with Large Numerical Arrays'
import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([6,5,7,8])
print(ax*2)
print(ax+18)

print(ax+ay)

# can use a map-function to an array
def f(x):
	return 3*x**2
print(f(ax))

import pprintpp as pp
# pp('321')



grid = np.zeros(shape = (1000, 1000), dtype = float)
print(grid)

a = np.array([
             [1,2,3,4], [5,6,7,8], [9,10,11,12]
	])

print(a)
# select 1 row, 1 col
print(a[0])
print(a[:, 0])

print(np.where(a < 10, a, 10) )

#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = ""

import numpy as np

ch = '3.10 Performing Matrix and Linear Algebra Calculations'

m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])

# Transpose
print(m.T)

# Inverse
print(m.I)

# create a vector and multiply

v = np.matrix([2,3,4]).T
print(v)

print(m*v)


# numpy.linalg subpackage


import numpy.linalg as la

# Determinant
print(la.det(m))

# Eigenvalues

print(la.eigvals(m))

# solve for x min mx = v
x = la.solve(m, v)
print(x)

ch = '3.11 Picking Things at Random'

import random
values = list(range(1,7))

print(random.choice(values))


# sample,

print(random.sample(values,4))

# shuffle
print(random.shuffle(values)) # None
random.shuffle(values)
print(values)

for _ in range(4):
	print(random.randint(0,10))


# uniform floating-point values in  0 - 1
print(random.random())

# get N random-bits
print(random.getrandbits(10))

#
ch = '3.12 Converting Days to Seconds, and other basic time conversions'