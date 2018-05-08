# -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:56:12 2018

@author: think
"""

from math import sqrt, exp, pi
import math

def print_row(lst):
    print (' '.join('%11.8f' % x for x in lst))

def romberg(f, a, b, eps=1e-6):
    """Approximate the definite integral of f from a to b by Romberg's method.
    eps is the desired accuracy."""
    print("T数表")
    R = [[0.5 * (b - a) * (f(a) + f(b))]]  # R[0][0]
    print_row(R[0])
    n = 1
    while True:
        h = float(b - a) / 2 ** n
#== 
#== Headline ==
#==
    
        R.append([None] * (n + 1))  # Add an empty row.
        # for proper limits
        R[n][0] = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1))
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4 ** m - 1)
        print_row(R[n])
        
        if abs(R[n][n-1] - R[n][n]) < eps:
            print("积分值")
            return R[n][n]
        n += 1

# In this example, the error function erf(1) is evaluated.
def f(x):
    return math.pow(math.e,-x) * math.sin(x) * math.sin(x)
#lambda t: math.sin(t)/t
print(romberg(f,0, 10))



