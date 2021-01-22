#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:15:05 2021

@author: fred
"""

#def test_profile(slow=True):
# Import required librariesimpo
import numpy as np
from numpy.polynomial.polynomial import polyfit
from numpy.polynomial import Polynomial as poly

def fun(x):
    return x**2+np.sin(x)-1
   
x = np.random.rand(100,100)
y = np.zeros_like(x)
IT1 = range(x.shape[0])
IT2 = range(x.shape[1])
slow = True 
if slow == True:
    for i in IT1:
        for j in IT2:
            coef = polyfit([0, 1, 4, 5],[-1, 2, 1, 4],3)
            p=poly(coef)
            y[i,j]=fun(x[i,j])/2 + p(x[i,j])
else:
    coef = polyfit([0, 1, 4, 5],[-1, 2, 1, 4],3)
    p=poly(coef)
    for i in IT1:
        for j in IT2:
            y[i,j]=fun(x[i,j])/2 + p(x[i,j])
