#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = ""

import numpy as np

ch = 'Performing Matrix and Linear Algebra Calculations'

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