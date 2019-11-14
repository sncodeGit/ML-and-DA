# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:23:39 2019

@author: inter000
"""

import math
import numpy as np
import matplotlib.pyplot as plt 
from scipy import optimize

def f(x):
    return math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)

X = np.arange(1, 30, 0.01)
plt.plot(X, list(map(f, X)))
plt.show()

print("Nelder-Mead: [X0] [Result function value] [Result X]")
for x0 in [5, 9, 10, 15, 25, 30]:
    res = optimize.minimize(f, x0, method='Nelder-Mead')
    print(x0, res.fun, res.x)

print("\nBFGS with X0 = 2: [Result function value] [Result X]")
res = optimize.minimize(f, 2, method='BFGS')
print(res.fun, res.x)

print("\nBFGS with X0 = 30: [Result function value] [Result X]")
res = optimize.minimize(f, 30, method='BFGS')
print(res.fun, res.x)