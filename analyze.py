#!/usr/bin/python
from __future__ import division, print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks_cwt
import os.path
import peakutils
from scipy.optimize import curve_fit

#shell
if len(sys.argv) != 3:
	quit('Usage: .//analyze.py <show|save> <spectrum.dat>')

if not os.path.isfile(sys.argv[2]):
	quit('The specified file does not exist.')

#load data
X, Y = np.loadtxt(sys.argv[2], unpack=True)

#plot data
plt.plot(X, Y, linewidth=0.1)
plt.xlabel(r'wavenumber in $cm^{-1}$')
plt.ylabel('optical density')
plt.grid()

#peak detection
indexes	= peakutils.indexes(Y, thres=0.02/max(Y), min_dist=55)

#mark peaks
plt.plot(X[indexes], Y[indexes], ls='', marker='o', markersize=2, color="red")

#find index of lowest peak
wmin=10
argmin = 0

indexes = indexes[5:-3] #first and last few peaks are just noise, cut those off, f*** the police

for i in indexes:
	if Y[i] < wmin:
		wmin = Y[i]
		argmin = i

#mark lowest peak
plt.plot(X[argmin], Y[argmin], marker='o', markersize=2, color='xkcd:teal')

#print lowest wavenumber
print('omega_0 =%.2f' %X[argmin], '\n')

#print p-branch
j=1
print('p-branch:\nwaveno.[cm^-1]\tj0\tj1')
for i in indexes:
	if X[i] < X[argmin]:
		print('%.2f\t\t%i\t%i' %(X[i], j, j-1))
		j=j+1

#print r-branch
j=0
print('\nr-branch:\nwaveno.[cm^-1]\tj0\tj1')
for i in indexes:
	if X[i] > X[argmin]:
		print('%.2f\t\t%i\t%i' %(X[i], j, j+1))
		j=j+1

#prepare peak diffs
#slice indexes (comparing to output of procedure above to find indexes)
indexes_p = indexes[:12]	#TODO: Remove hard-coded shit.
indexes_r = indexes[13:]	#TODO: Remove hard-coded shit.
diff_p = np.zeros(indexes_p.size-1)
diff_r = np.zeros(indexes_r.size-1)

#calculate difffs
for i in range(0, len(indexes_p)-1):
	diff_p[i]=X[indexes_p[i+1]]-X[indexes_p[i]]
for i in range(0, len(indexes_r)-1):
	diff_r[i]=X[indexes_r[i+1]]-X[indexes_r[i]]

print('\ndiffs of p-branch:\n', diff_p, '\n')
print('\ndiffs of r-branch:\n', diff_r, '\n')

#fit
def pbranch(j, B0, B1):
	return 2*B0 + 2*(B0-B1)*j

def rbranch(j, B0, B1):
	return 2*(2*B1-B0)+2*(B1-B0)*j

X_p = np.arange(0, len(indexes_p)-1, 1)
X_r = np.arange(0, len(indexes_r)-1, 1)

poptp, pcovp = curve_fit(pbranch, X_p, diff_p)
poptr, pcovr = curve_fit(rbranch, X_r, diff_r)

print('p-branch: B0 = %.2f,\tB1 = %.2f' %(poptp[0], poptp[1]))
print('r-branch: B0 = %.2f,\tB1 = %.2f' %(poptr[0], poptr[1]))
#shell
if sys.argv[1].lower() == 'show':
	plt.show()
elif sys.argv[1].lower() == 'save':
	plt.savefig('%s.pdf' %sys.argv[2][:-4])
else:
	quit('Usage: .//analyze.py !>>> <show|save> <<<! <spectrum.dat>')
