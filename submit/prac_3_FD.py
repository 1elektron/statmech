# using fermi dirac statistic
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

N = np.array([1,2,3]) # number of paticles 

n = 3  # number of energy levels
dE = 0.01 # ev
E0 = 0 # ground state energy
E1 = E0 + dE # first state nergy
E2 = E0 + 2*dE # second state nergy

# Z_list to store value of partition fucntion
# at differnt temperatures for differnt number of
# particles

Z_list = np.zeros((len(N),len(T))) # row,col


def Z1(t):
    # partition funciton for 1 particle and 3 levels
    # t is temp
    b = (e/k)/t
    return np.e**(-E0*b) + np.e**(-E1*b) + np.e**(-E2*b)

def Z2(t):
    # partitio function for 2 partilces and 3 levels
    # t is temp
    b = (e/k)/t
    return (np.e**(-(E0 + E1)*b) + np.e**(-(E0 + E2)*b) + 
            np.e**(-(E1 + E2)*b) )

def Z3(t):
    # partitio function for 3 partilces and 3 levels
    # t is temp
    b = (e/k)/t
    return np.e**(-(E0 + E1 + E2 )*b) 

for j in range(len(T)):

    # row0 stores partition function for 1 particle
    # row1 for 2 paticles and row2 for 3 .
    Z_list[0,j] = Z1(T[j])
    Z_list[1,j] = Z2(T[j])
    Z_list[2,j] = Z3(T[j])


# Energy
T1 = T[:-1]
U = k*T1*T1*np.diff(np.log(Z_list))/dT

# specific heat capacity
T2 = T1[:-1]
Cv = np.diff(U)/dT

# Helomholtz free energy 
F = -k*T*np.log(Z_list)

# enrtopy
S = -np.diff(F)/dT

# plot
plt.figure(1)
plt.xlabel('T(K)')
plt.ylabel('Average Energy (J)')
plt.plot( T1, U[0] , label ='N(particle) =1  ')
plt.plot( T1, U[1] , label ='N=2')
plt.plot( T1, U[2] , label ='N=3')
plt.legend()

plt.figure(2)
plt.xlabel('T(K)')
plt.ylabel('Heat Capactiy (J/K)')
plt.plot(T2,Cv[0] , label ='N(particle) =1')
plt.plot(T2,Cv[1] , label ='N=2')
plt.plot(T2,Cv[2] , label ='N=3')
plt.legend()


plt.figure(3)
plt.xlabel('T(K)')
plt.ylabel(' Entropy (J/K)')
plt.plot(T1,S[0] , label ='N(particle) =1')
plt.plot(T1,S[1] , label ='N=2')
plt.plot(T1,S[2] , label ='N=3')
plt.legend()

plt.figure(5)
plt.xlabel('T(K)')
plt.ylabel(' Partiton  Function Z')
plt.plot(T,Z_list[0], label = 'N(particle) =1')
plt.plot(T,Z_list[1], label = 'N =2')
plt.plot(T,Z_list[2], label = 'N =3')
plt.legend()
plt.show()
