import numpy as np

def Spannungsrechn(U, U0):
    U = (U - U0)*1000
    U = np.sqrt(U)
    return(U)

n = int(input("Anzahl der Messwerte: "))
U0 = float(input("U0: "))*1000
dU0 = float(input("Fehler von U0: "))*1000
values = np.zeros(n)
dU = np.zeros(n)


i = 0
for i in range(n):
    print("\nWert ", i+1, " eingeben: ")
    values[i] = input()
    i += 1
values_u = values*1000

for i in range(n):
    if values_u[i] < 100:
        dU[i] = np.sqrt((0.003*values_u[i])**2+(0.0008*values_u[i])**2+(15)**2)
    else:
        dU[i] = np.sqrt(((0.003*values_u[i])**2)+((0.0008*values_u[i])**2)+((5)**2))
    print("\nU ", i+1, " = ", round(values_u[i], 1), " ± ", round(dU[i], 1), " mV")
    i += 1

    
for i in range(n):
    dU[i] = np.sqrt((0.003*values_u[i])**2+(0.0008*values_u[i])**2+(15)**2)
    values[i] = Spannungsrechn(values[i], U0/1000)
    dU[i] = (1/(2*np.sqrt(values_u[i]-U0)))*np.sqrt(dU[i]**2+dU0**2)
    print("\nsqrt(U-U0) ", i+1, " = ", round(values[i], 1), " ± ", round(dU[i], 1), " mV")
    i += 1
