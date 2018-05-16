#!/bin/python3
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys

""" Constants """
l = 50	#in cm
n = 1.0014	#refractive index of detector
m_p = 0.93827203	#proton rest mass in GeV
m_k = 0.497648		#kaon rest mass in GeV
m_pi = 0.13957018	#pion rest mass in GeV

def R(p, m):
	return l * np.sqrt( (n*p)**2 / (p**2 + m**2) - 1 )

X = np.linspace(0, 30, 1000)
Yp = R(X, m_p)
Yk = R(X, m_k)
Ypi = R(X, m_pi)

plt.plot(X, Yp, label='proton')
plt.plot(X, Yk, label='kaon')
plt.plot(X, Ypi, label='pion')
plt.xlabel('$p$ in GeV')
plt.ylabel('$R(p)$ in cm')
plt.grid()
plt.legend()

if len(sys.argv) == 2 and sys.argv[1] == 'show':
	plt.show()
elif len(sys.argv)==3 and sys.argv[1] == 'save':
	plt.savefig(sys.argv[2])
