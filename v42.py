import numpy as np

i=0

def g_force(m): #calculate the gravitational force, exerting to the plate
	F = m*9.81
	return(F)

def error_bars(n ,r, F ,angular, dangular, dr):
	
	uncertainty = np.sqrt((F*dr/angular)**2+(F*r*dangular/angular**2)**2)
	return(uncertainty)


def calc(n):
	r = 5.03 #could have done with an input function too
	D = np.zeros(n)
	print("Enter the masses: ")
	mass = np.zeros(n)
	for i in range(n): #for loop to collect masses
		print("m", i+1,"= ")
		mass[i] = input()
	print("Enter angulars: ")
	angular = np.zeros(n)
	for i in range(n): #for loop to collect angular
		print("phi",i+1,"= ")
		angular[i] = input()
	D = (g_force(mass)*r/angular)
	return(D, angular, mass)

def calc_D(n):
	#change the uncertainties here:
	dr = 0.0001
	dangular = 1
	r = 0.0503
	D, angular, mass = calc(n)
	uncertainty = error_bars(n,r , g_force(mass), angular, dangular, dr)
	for i in range(n):
		print("D = ", D[i], " +- ", uncertainty[i])

def calc_M(n):
	dr = 0.0001
	r = 0.0503
	mass = np.zeros(n)
	for i in range(n): #for loop to collect masses
		print("m", i+1,"= ")
		mass[i] = input()
	M = g_force(mass)*r
	for i in range(n):
		print("M= ", M[i], " +- ", dr)
	
print("Enter the amount of taken measurements: ")
n = int(input())

#calc_D(n)
calc_M(n)
