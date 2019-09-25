import numpy as np
import matplotlib.pyplot as plt

def inpt_msmts():     #input function to recognize the number of data
    print("Fehlerrechner v. 1.0  ©Tom Schlenker\n")
    msmts = int(input("Please enter the amount of measurements: "))
    return(msmts)

def inpt_values():      #input function for each value
    values = np.zeros(msmts)
    print("Please enter in the following step the value for each measurement.")
    i = 0
    while i < msmts:
        print("Please enter value", i+1, ":  ")
        values[i] = input()
        i += 1
    return(values)

def norm_const():
    norm_const = int(input("Please enter a normalization constant (1 if not known): "))
    return(norm_const)

def mean(msmts, values):        #define x_
    msmts = float(msmts)
    mean_c = (1/msmts*np.sum(values))
    return(mean_c)

def stdrddev_single(msmts, values, mean):       #define standard deviation for one measurement
    i = 0
    values_n = np.zeros(msmts)
    while i < msmts:
        values_n[i] = (values[i] - mean)**2
        i += 1
    summed_values = np.sum(values_n)
    stdrddev_single_c = (1/(msmts-1)*(summed_values))**(1/2)
    return(stdrddev_single_c)

def stdrddev_all(msmts, stdrddev_single_c):      #define sigma
    msmts = float(msmts)
    stdrddev_all_c = (1/np.sqrt(msmts))*stdrddev_single_c
    return(stdrddev_all_c)

def mesaured_var(mean_c, stdrddev_single_c):
    print("The calculated measured variable is: ")


msmts = inpt_msmts()
values = (inpt_values()/norm_const())
mean = mean(msmts, values)
stdrddev_single = stdrddev_single(msmts, values, mean)
stdrddev_all = stdrddev_all(msmts, stdrddev_single)
print("\n\n\n", "Messwerte: ", values)
print("\nMittelwert der Werte: ", mean)
print("Standardabweichung der Einzelmessung: ", stdrddev_single)
print("Standardabweichung des Mittelwertes: ", stdrddev_all)
print("Messgröße: ", mean, "±", stdrddev_all)
print("Statistische Messunsicherheit: ", 1/(np.sqrt(msmts)))

systematic_error=0
yerror = max(stdrddev_single, systematic_error)
xaxis = np.arange(1, msmts+1, 1)

plt.plot(xaxis, values, 's')
plt.errorbar(xaxis, values, yerr=yerror, fmt= ' ', elinewidth=2, capsize=5)
plt.title("Messwerte mit Fehler")
plt.xlabel("Messung")
plt.ylabel("Messwert")

n, bins, patches = plt.hist(x=values, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

numbs = np.arange(mean-10*stdrddev_all, mean+10*stdrddev_all, stdrddev_all/20)
gauss = 1/(stdrddev_all*(2*np.pi)**(1/2))*np.exp((-(numbs-mean)**2)/(2*stdrddev_all**2))
plt.plot(numbs, gauss)

plt.show()
