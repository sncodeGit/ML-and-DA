# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 00:30:58 2019

@author: inter000
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)

def polinomial(coef, x):
    res = 0
    i = 0
    for w in coef:
        res += w * (x ** i)
        i += 1
    return res
    
# Многочлен первой степени
A = np.array([[1,1], [1, 15]])
b = np.array([f(1), f(15)])
x1 = linalg.solve(A,b)

# Многочлен второй степени
A = np.array([[1, 1, 1], [1, 8, 64], [1, 15, 225]])
b = np.array([f(1), f(8), f(15)])
x2 = linalg.solve(A,b)

# Многочлен третьей степени
A = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])
b = np.array([f(1), f(4), f(10),  f(15)])
x3 = linalg.solve(A,b)

X = np.arange(1, 15, 0.01)
plt.plot(X, list(map(f, X)),  color = 'g')
plt.plot(X, list(map(lambda x: polinomial(x1, x), X)))
plt.plot(X, list(map(lambda x: polinomial(x2, x), X)))
plt.plot(X, list(map(lambda x: polinomial(x3, x), X)), color = 'r')
        
plt.show()
         
print(x3)