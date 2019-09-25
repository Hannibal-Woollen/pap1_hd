import numpy as np

mw = np.array([616.48, 615.3, 614.72])
cw = 4.186
W = 79.8
T_T2 = np.array([28.4 - 22.7, 31.3 - 28, 34.7 - 30.8])
mx = np.array([155.53, 602.34, 123.14])
T1_T = np.array([100-28.4, 100-31.3, 100-34.7])
dmw = np.sqrt(2*0.05**2)
dcw = 0.004
dW = 8
dT_T2 = np.sqrt(0.2**2+0.1**2)
dmx = 0.05
dT1_T = dT_T2 #input could be defined more beautifully with input() functions, but would be about (300+-50)% more annoying

cx = (((mw*cw+W)*(T_T2))/(mx*T1_T))
therm1 = ((cw+W)*T_T2*dmw/(mx*T1_T))**2
therm2 = ((mw+W)*T_T2*dcw/(mx*T1_T))**2
therm3 = ((cw*mw*T_T2*dW/(mx*T1_T)))**2
therm4 = ((cw*mw+W)*dT_T2/(mx*T1_T))**2
therm5 = ((cw*mw+W)*T_T2*dmx/((mx**2)*T1_T))**2
therm6 = ((cw*mw+W)*T_T2*dT_T2/(mx*(T1_T)**2))**2 

dcx = np.sqrt(therm1+therm2+therm3+therm4+therm5+therm6)

for i in range(3):
	print("cx = ", cx[i], " +- ", dcx[i])
