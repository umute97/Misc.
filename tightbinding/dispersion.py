#!/usr/bin/python
from __future__ import division, print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

res = 100
a = 1
k_range = np.linspace(-2*np.pi/a, 2*np.pi/a, res)
kx, ky = np.meshgrid(k_range, k_range)

def energyfunc(kx, ky, a):

	return np.cos(kx*a) + np.cos(ky*a)

def energygrad(kx, ky, a):

	return -a* (np.sin(kx*a) + np.sin(ky*a))

fig, ax = plt.subplots()

levels = np.arange(-2, 2.25, 0.25)
tick_labels = []
for i in np.arange(-2, 2.5, 0.5):
	lbl = '%.1f$\\pi$' %i
	print(lbl)
	tick_labels.append(lbl)

cs = ax.contour(kx, ky, energyfunc(kx, ky, 1), levels=levels)
ax.set_xticks(np.arange(-2*np.pi/a, 2*np.pi/a + np.pi/a/2, np.pi/a/2))
ax.set_yticks(np.arange(-2*np.pi/a, 2*np.pi/a + np.pi/a/2, np.pi/a/2))
ax.set_xticklabels(tick_labels)
ax.set_yticklabels(tick_labels)
ax.set_xlabel("$\\frac{k_x}{a}$")
ax.set_ylabel("$\\frac{k_y}{a}$")

cb = fig.colorbar(cs, ax=ax, format='%.2f')
cb.set_label('Energy $\\hat{E}$')

plt.savefig('dispersion.pdf')
