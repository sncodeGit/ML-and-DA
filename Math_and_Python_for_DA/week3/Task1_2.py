# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:10:32 2019

@author: inter000
"""

import math 
from scipy import optimize

def f(x):
    return math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)

print("\n\nDifferential Evolution:\n\n", optimize.differential_evolution(f, ([1, 30],)))
print("\n\nBFGS witg X0 = 11:\n\n", optimize.minimize(f, 11, method='BFGS'))
print("\n\nBFGS witg X0 = 20:\n\n", optimize.minimize(f, 20, method='BFGS'))
print("\n\nBFGS witg X0 = 25:\n\n", optimize.minimize(f, 25, method='BFGS'))