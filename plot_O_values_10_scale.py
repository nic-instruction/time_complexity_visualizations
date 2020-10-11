#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

X = np.linspace(0, 10, 10)

plt.yticks(np.linspace(0, 10, 10))
plt.ylim(0, 10)

Ya = (X)
Yb = (X**2)
Yc = (X*np.log(X))
Ye = (np.log(X))
Yf = (gamma(X))
Yg = (2**X)

line1, = plt.plot(X, Ya, marker='o', label='O(n)')
line2, = plt.plot(X, Yb, marker='o', label='O(n^2)')
line3, = plt.plot(X, Yc, marker='o', label='O(nlog(n))')
line5, = plt.plot(X, Ye, marker='o', label='O(log(n))')
line6, = plt.plot(X, Yf, marker='o', label='O(n!)')
line7, = plt.plot(X, Yg, marker='o', label='O(2^n)')

plt.legend()
plt.show()
