#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"

'4.3 Creating New Iteration Patterns with Generators'

'''
	Problem
	You want to implement a custom iteration pattern that’s different than the usual built-in functions (e.g., range(), reversed(), etc.).
'''

def frange(start, stop, increment):
	x = start
	while  x < stop:
		yield x
		x += increment


# range() integer step argument expected, got float.
# for x in range(0,40, 0.5): print x,

for n in frange(0, 40, 0.5): print n,

print '-'*28
print list(frange(0,10,1.5))



def countdown(n):
	print('Starting to count from', n)
	while n > 0:
		yield n
		n -= 1
	print ('Done!')

# create the generator, notice no output appears

c = countdown(3)
print c

# Run to first yield and emit a value
print next(c)
print next(c)
print next(c)

print next(c) # StopIteration

