#!/usr/bin/python
from __future__ import division, print_function
import numpy as np
import itertools
import matplotlib.pyplot as plt
import sys

#constants
wl = 3.62
wt = 5
e  = 2.25

#functions to plot
def epsilon(x, wl, wt, e):
	return e*(wl**2-x**2)/(wt**2-x**2)

def R(x, wl, wt, e):
	return (np.sqrt(epsilon(x, wl, wt, e))-1)**2/(np.sqrt(epsilon(x, wl, wt, e))+1)**2

#plot
X = np.linspace(0, 10*wt, 1000)
plt.plot(X, R(X, wl, wt, e))
plt.xlabel('$\\omega$ in THz')
plt.ylabel('$R(\\omega)$')
plt.grid()

if len(sys.argv) == 2 and sys.argv[1] == 'show':
	plt.show()
elif len(sys.argv)==3 and sys.argv[1] == 'save':
	plt.savefig(sys.argv[2])
