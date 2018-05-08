# -*- coding: utf-8 -*-
"""
Created on Thu May  3 23:24:39 2018

@author: think
"""
import math
from scipy.interpolate import lagrange

l = [math.cos((2 * i + 1)*math.pi/(2 * 20 + 1)) for i in range(0,20)]
j = [math.pow(x,0.5) for x in l]

#math.pow(math.e,x)
#1/(x * x + 1)
a = lagrange(l,j)
print("函数")
print(a)
print("插值点")
print(l)
print("函数值")
print(j)
print("由插值函数计算得的值")
print(a(5),a(50),a(115),a(185))


