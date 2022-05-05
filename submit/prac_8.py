#To do:
# Plot enrgy/vol-frq
# Plot energy/vol

from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#constants actual
c = 3*10**8 # m/s
h = 6.626*(10**(-34)) # J-s
k = 1.381*10**(-23) #J/K
lamb_max = 2000 # nm 
nu_max = 10
beta = h*c/k
T1 = 2000 # K
T2 = 4000 # K
T3 = 6000 # K



def  planck_dist_lamb(lamb,T):
    cons = 8*np.pi*h
    return cons/((lamb**3)*(np.exp(h*c/(lamb*k*T))-1))

def  planck_dist_nu(nu,T):
    cons = 8*np.pi*h
    return (cons*(nu/c)**3)/(np.exp(h*nu/(k*T))-1)

def r_j_dist_nu(nu,T):
    return (8*np.pi*k*T*nu**2)/c**3

def wein_dist_nu(nu,T):
    cons = 8*np.pi*h
    return (cons*(nu/c)**3)/np.exp(h*nu/(k*T))
# lamb_array = np.linspace(10**-2,lamb_max,1000)


#------------Placnck--------------------------------------------------
nu_array = 10**14*np.linspace(0.001,nu_max,100)
plt.xlim((0,nu_max))
plt.ylim((0,2))

#----------------------Planck's law--------------
# plt.plot(nu_array/10**14,10**15*planck_dist_nu(nu_array,T1))
# plt.plot(nu_array/10**14,10**15*planck_dist_nu(nu_array,T2))
plt.plot(nu_array/10**14,10**15*planck_dist_nu(nu_array,T3),label='Planck \' s Law')
# -----------------------------------------------

#-----------Rayleigh_jeans----------------------
# plt.plot(nu_array/10**14,10**15*r_j_dist_nu(nu_array,T1),ls='--')
# plt.plot(nu_array/10**14,10**15*r_j_dist_nu(nu_array,T2),ls='--')
plt.plot(nu_array/10**14,10**15*r_j_dist_nu(nu_array,T3),ls='--',label='Rayleigh-Jeans Law')

#----------Wein-----------------------------------
# plt.plot(nu_array/10**14,10**15*wein_dist_nu(nu_array,T1),ls=':')
# plt.plot(nu_array/10**14,10**15*wein_dist_nu(nu_array,T2),ls=':')
plt.plot(nu_array/10**14,10**15*wein_dist_nu(nu_array,T3),ls=':',label='Weins\' Law')
#-------------------------------------------------


# plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = '13'
plt.grid(True)
plt.xlabel(r'$\nu 10^{-14}  $ frequency',fontsize=14)
plt.ylabel(r'$u(\nu ,T) \cdot 10^{15}  \ \ J / {m^3 s} $  ',fontsize=14)
plt.legend()
plt.show()
