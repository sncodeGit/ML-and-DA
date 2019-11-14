# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:26:23 2019

@author: inter000
"""

import math
import numpy as np
import matplotlib.pyplot as plt 
from scipy import optimize

def f(x):
    return math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)

def h(x):
    return int(f(x))

X = np.arange(1, 31, 0.01)
plt.plot(X, list(map(h, X)))
plt.show()

print("\n\nBFGS with X0 = 30:\n\n", optimize.minimize(h, 30., method='BFGS'))
print("\n\nBFGS with X0 = 25.1:\n\n", optimize.minimize(h, 25.1, method='BFGS'))
# Градиент (производная, т.к. случай одномерный) нулевой =>
# BFGS даже не совершит ни одной итерации
print("\n\nDifferential Evolution:\n\n", optimize.differential_evolution(h, ([1, 30],)))