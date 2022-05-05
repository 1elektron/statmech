import numpy as np
import matplotlib.pyplot as plt

#constants , 1eV = e * (1 J)
k = 1.381*10**(-23) # J/K
e = 1.602 * 10**(-19) # coulomb

# create temperature points
Tmin = 1
Tmax = 500
dT = 0.1
T =  np.arange(Tmin,Tmax + 1,dT)

N = np.array([100,200,300]) # number of paticles 

n = 3  # number of energy levels
E0 = 0 # ground state energy
dE = 0.01 # ev

# Z_list to store value of partition fucntion
# at differnt temperatures for differnt number of
# particles

Z_list = np.zeros((len(N),len(T)))

# P list stoes the value of boltzmann factors of each
# state at a given temp as column, next column for next
# temp and so on. And then each colum is divided by the
# partiton function at that temp to convert those 
# boltzmann factor into probabilities.

P_list = np.zeros((len(N),len(T)))

for m in range(len(N)):
    for j in range(len(T)):
        z = 0 # partition function for each particle
        for i in range(n):

            # print((e/k)/(T[j]))
            P_list[i,j] = np.e**(-(E0 + i*dE)*(e/k)/(T[j]))
            z = z + P_list[i,j]
        
        # the partition function for N partices is just
        Z_list[m,j] = z**N[m]
        P_list[:,j] = P_list[:,j]/z

T1 = T[:-1]
# note that multiplicatio of 2D array and 1D array
# first elemt of T is multiplied to first element
# of all rows (first column that is). That what we need.
U = k*T1*T1*np.diff(np.log(Z_list))/dT

# specific heat capacity
T2 = T1[:-1]
Cv = np.diff(U)/dT

# Helomholtz free energy 
F = -k*T*np.log(Z_list)
S = -np.diff(F)/dT

#plot
plt.figure(1)
plt.xlabel('T(K)')
plt.ylabel('Average Energy (J)')
plt.plot( T1, U[0] , label ='N='+str(N[0]))
plt.plot( T1, U[1] , label ='N='+str(N[1]))
plt.plot( T1, U[2] , label ='N='+str(N[2]))
plt.legend()

plt.figure(2)
plt.xlabel('T(K)')
plt.ylabel('Heat Capactiy (J/K)')
plt.plot(T2,Cv[0] , label ='N='+str(N[0]))
plt.plot(T2,Cv[1] , label ='N='+str(N[1]))
plt.plot(T2,Cv[2] , label ='N='+str(N[2]))
plt.legend()


plt.figure(3)
plt.xlabel('T(K)')
plt.ylabel(' Entropy (J/K)')
plt.plot(T1,S[0] , label ='N='+str(N[0]))
plt.plot(T1,S[1] , label ='N='+str(N[1]))
plt.plot(T1,S[2] , label ='N='+str(N[2]))
plt.legend()

plt.figure(4)
plt.xlabel('T(K)')
plt.ylabel('Probability of occupancy (J)')
plt.plot(T,P_list[0] , label ='State 0')
plt.plot(T,P_list[1] , label ='State 1')
plt.plot(T,P_list[2] , label ='State 2')

plt.legend()
plt.show()
