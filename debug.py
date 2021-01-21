#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:19:08 2021

@author: fred
"""
import numpy as np
import matplotlib.pyplot as plt

size = 20
z = np.zeros(size)

for i in range(size):
    z[i] = i**2 + 4

plt.plot(range(size),z)