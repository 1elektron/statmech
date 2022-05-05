import numpy as np
import matplotlib.pyplot as plt
e = np.e
k = 8.617*10**(-5)

T1 = 300   # K
T2 = 500  # K
T3 = 800 # K

def Boltzmann_stat(x,T):
    a=k*T
    return e**(-x/a)

def Bose_Einstein_stat(x,T):
    a=k*T
    return 1/(e**(x/a) - 1)

def Fermi_Dirac_stat(x,T):
    a=k*T
    return 1/(e**(x/a) + 1)

# x = enegy minus chemical potential
len = 160
x = np.linspace(-0.5,0.5,len)

plt.figure(0)
plt.title('At T=300K')
plt.plot(x,Boltzmann_stat(x,T1),label='Bolz.')
plt.plot(x[len//2 + 1 : ],Bose_Einstein_stat(x[len//2 + 1 : ],T1),label='B-E')
plt.plot(x,Fermi_Dirac_stat(x,T1),label='F-D')
plt.ylim(-0.1,1.5)
plt.grid(True)
plt.xlabel(r'$\epsilon - \mu$ eV')
plt.ylabel(r'$\bar{n}$')
plt.legend()


plt.figure(1)
plt.title('At T=500K')
plt.plot(x,Boltzmann_stat(x,T2),label='Bolz.')
plt.plot(x[len//2 + 1 : ],Bose_Einstein_stat(x[len//2 + 1 : ],T2),label='B-E')
plt.plot(x,Fermi_Dirac_stat(x,T2),label='F-D')
plt.ylim(-0.1,1.5)
plt.grid(True)
plt.legend()
plt.xlabel(r'$\epsilon - \mu$ eV')
plt.ylabel(r'$\bar{n}$')



plt.figure(2)
plt.title('At T=800K')
plt.plot(x,Boltzmann_stat(x,T3),label='Bolz.')
plt.plot(x[len//2 + 1 : ],Bose_Einstein_stat(x[len//2 + 1 : ],T3),label='B-E')
plt.plot(x,Fermi_Dirac_stat(x,T3),label='F-D')
plt.ylim(-0.1,1.5)
plt.grid(True)
plt.legend()


plt.xlabel(r'$\epsilon - \mu$ eV')
plt.ylabel(r'$\bar{n}$')
plt.show()