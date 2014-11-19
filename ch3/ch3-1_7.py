'ch3 Numbers Dates and Times'

'3.1 - 3.5'

'3.1 Rounding Numerical Values'

'Pythonds 2.x'

rawnumber = 1.234
print(round(rawnumber, 1)) # 1.2
print(round(rawnumber, 2)) # 1.23
print(round(rawnumber, 3)) # 1.234
print(round(rawnumber, 5)) # 1.234

print(round(1.5,0)) # 2.0
print(round(2.5,0)) # 3.0


# use format()

x = 1.23456
print(format(x,'0.2f')) # 1.23
print(format(x,'0.3f')) # 1.235

print(6-3)


'3.2 Performing Accurate Calculation'

print(3.2+3.1 == 6.3) # False

from decimal import Decimal
a = Decimal('3.2')
b = Decimal('3.1')
c = a + b
print (c == Decimal('6.3')) # True


print(a/b)
# 1.032258064516129032258064516

# control precise
from decimal import localcontext
with localcontext() as ctx:
	ctx.prec = 3
	print(a/b) # 1.03


with localcontext() as ctx:
	ctx.prec = 30
	print(a/b) # 1.03



'3.3 Formatting Numbers for Output'

print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, 'e'))
print(format(x, '0.2E'))


'3.4 Working with Binary, Octal, and Hexadecimal Integers'


'3.5 Packing and Unpacking Large Integers from Bytes'

'3.6 Performing Complex-Valued Math'
a = complex(3,4)
b = 3-5j
print(a+b)
'3.7 Working with Infinity and NaNs'

a = float('inf')
b = float('-inf')
c = float('nan')
print(a>2)
print(a>b) # True
print(a>c) # False


'3.8 Calculating with Fractions'

from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)

print(a+b)

#
# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)



