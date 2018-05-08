# -*- coding: utf-8 -*-
"""
Created on Fri May  4 09:42:23 2018

@author: think
"""
def le(n,x):
    if(n  == 0): return 1
    elif(n == 1): return x
    return le(n - 1,x) * x * (2 * n - 1)/n - le(n - 2,x) * (n-1)/n

print(le(2,x))