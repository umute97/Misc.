#!/usr/bin/python
from __future__ import division, print_function
import numpy as np
import itertools
import matplotlib.pyplot as plt
#import peakutils

#lattice constants in A
nmax = 3
dim = 3
a = 4.594
c = 2.959
lamb = 1.54056

d = np.zeros((dim, dim, dim))

for h in range(0, dim):
	for k in range(0, dim):
		for l in range(0, dim):
			d[h][k][l] = 1 / np.sqrt( (1/a**2)*(h**2+k**2) + (l/c)**2 )

twotheta = 2*np.arcsin(lamb/(2*d))

for n in range(0, nmax):
	print('%i-th order:' %n)
	for h in range(0, dim):
		for k in range(0, dim):
			for l in range(0, dim):
				print('(%i, %i, %i): %.2f' %(h, k, l, twotheta[h][k][l]*180/np.pi))

#plot of spectrum
angle, intensity = np.loadtxt('data.txt', unpack=True)
plt.plot(angle, intensity, color='blue')
plt.xlabel('$2\\theta$ in $\\degree$')
plt.ylabel('intensity in a.u.')

# #peak detection
# indexes	= peakutils.indexes(Y, thres=0.02/max(Y), min_dist=55)
#
# #mark peaks in spectrum
# for i in indexes:
# 	plt.plot(angle[i], intensity[i], fmt='o', color='red')
#
# print('==========================================\npeak angles[deg]:')
# for i in indexes:
# 	print(angle[i])

plt.savefig('braggspectrum.pdf')
