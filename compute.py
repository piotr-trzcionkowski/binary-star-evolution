#!/usr/bin/env python3

import numpy as np
import sys
import subprocess

#f = open("collected.data", 'w')
#f.write("#      Tmax       M1       M2 log10(P)   e\n")
#f.close()

M1 = 0.7
M2 = 1.5
T = [3000, 5000]
e = [0.0, 0.2, 0.4, 0.6, 0.8]

def calc(M1, M2, T, e):
	for i in range(2):
		f = open("collected%i.data" %T[i], 'w')
		f.write("#     Tmax k1 k2 log10(P)   e\n")
		for j in range(5):
			for P in np.logspace(0, 3.5, num=100):
				b = open("binary.in", 'w')
				b.write("%f %f %f %f 1 1 0.001 %f\n" % (M1, M2, T[i], P, e[j]))
				b.write("0.5 0.0 1.0 3.0 0.5\n")
				b.write("0 1 0 1 0 1 3.0 29769\n")
				b.write("0.05 0.01 0.02\n")
				b.write("190.0 0.125 1.0 1.5 0.001 10.0 -1.0\n")
				b.close()
				subprocess.call("./bse")

				TMax, k1, k2= np.genfromtxt("binary.dat", usecols=(0, 1, 2), skip_footer=2, unpack=True)
				d=-1
				#print(TMax[d], T[i])
				while (TMax[d] == -1):
					d=d-1
				f.write("%f %i %i %f %.1f\n" % (T[i], k1[d], k2[d], np.log10(P), e[j]))
		f.close()

calc(M1, M2, T, e)

M1 = 10
M2 = 20
T= [5, 100]

calc(M1, M2, T, e)