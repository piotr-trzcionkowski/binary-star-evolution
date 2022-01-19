#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def wykres(TMAX, M1, M2):
	T, k1, k2, logP, e = np.loadtxt("collected%i.data"%TMAX, unpack=True)
	D=500

	plt.figure(figsize=(14,12))
	x =np.zeros(D)
	y =np.zeros(D)
	#star-star
	j=0
	for i in range(D):
		if (k1[i] <= 9) and (k2[i] <= 9):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "star-star", color='red')


	x =np.zeros(D)
	y =np.zeros(D)
	#star-WD
	j=0
	for i in range(D):
		if ((k1[i] <= 9) and (k2[i] in [10, 11, 12])) or ((k2[i] <= 9) and (k1[i] in [10, 11, 12])):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "star-WD", color='blue')

	x =np.zeros(D)
	y =np.zeros(D)
	#star-NS
	j=0
	for i in range(D):
		if ((k1[i] <= 9) and (k2[i] == 13)) or ((k2[i] <= 9) and (k1[i] == 3)):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "star-NS", color='orange')

	x =np.zeros(D)
	y =np.zeros(D)
	#star-BH
	j=0
	for i in range(D):
		if ((k1[i] <= 9) and (k2[i] == 14)) or ((k2[i] <= 9) and (k1[i] == 14)):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "star-BH", color='black')

	x =np.zeros(D)
	y =np.zeros(D)
	#single star
	j=0
	for i in range(D):
		if ((k1[i] <= 9) and (k2[i] == 15)) or ((k2[i] <= 9) and (k1[i] == 15)):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "single star", color='yellow')


	x =np.zeros(D)
	y =np.zeros(D)
	#WD-WD
	j=0
	for i in range(D):
		if ((k2[i] in [10, 11, 12]) and (k1[i] in [10, 11, 12])):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "WD-WD", color='green')


	x =np.zeros(D)
	y =np.zeros(D)
	#WD- NS
	j=0
	for i in range(D):
		if ((k1[i] == 13) and (k2[i] in [10, 11, 12])) or ((k2[i] == 13) and (k1[i] in [10, 11, 12])):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "WD-NS", color='darkorange')

	x =np.zeros(D)
	y =np.zeros(D)
	#WD-BH
	j=0
	for i in range(D):
		if ((k1[i] == 14) and (k2[i] in [10, 11, 12])) or ((k2[i] == 14) and (k1[i] in [10, 11, 12])):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "WD-BH", color='dimgray')

	x =np.zeros(D)
	y =np.zeros(D)
	#single WD
	j=0
	for i in range(D):
		if ((k1[i] == 15) and (k2[i] in [10, 11, 12])) or ((k2[i] == 15) and (k1[i] in [10, 11, 12])):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "single WD", color='cyan')

	x =np.zeros(D)
	y =np.zeros(D)
	#NS-NS
	j=0
	for i in range(D):
		if (k1[i] == 13) and (k2[i] == 13):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "NS-NS", color='red')

	x =np.zeros(D)
	y =np.zeros(D)
	#NS-BH
	j=0
	for i in range(D):
		if ((k1[i] == 14) and (k2[i] == 13)) or ((k1[i] == 13) and (k2[i] == 14)):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "NS-BH", color='orangered')

	x =np.zeros(D)
	y =np.zeros(D)
	#single NS
	j=0
	for i in range(D):
		if ((k1[i] == 15) and (k2[i] == 13)) or ((k1[i] == 13) and (k2[i] == 15)):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "single NS", color='saddlebrown')

	x =np.zeros(D)
	y =np.zeros(D)
	#BH-BH
	j=0
	for i in range(D):
		if (k1[i] == 14) and (k2[i] == 14):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "BH-BH", color='crimson')

	x =np.zeros(D)
	y =np.zeros(D)
	#single BH
	j=0
	for i in range(D):
		if ((k1[i] == 15) and (k2[i] == 14)) or ((k1[i] == 14) and (k2[i] == 15)):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "single BH", color='purple')

	x =np.zeros(D)
	y =np.zeros(D)
	#nothng
	j=0
	for i in range(D):
		if (k1[i] == 15) and (k2[i] == 15):
			x[j] = logP[i]
			y[j] = e[i]
			j+=1
	plt.plot(x, y, 'o', label= "nothing", color='lightgrey')
	
	plt.xlabel("log(P)")
	plt.ylabel("e")
	plt.title("Zaleznosc dla M1 = %.1f[M_Sol], M2 = %.1f[M_Sol], TMax = %i [Myr]"%(M1, M2, TMAX))
	plt.legend()
	plt.savefig("collected%i.png"%TMAX)
#	plt.show()

wykres(3000, 0.7, 1.5)
wykres(5000, 0.7, 1.5)
wykres(5, 10, 20)
wykres(100, 10, 20)

