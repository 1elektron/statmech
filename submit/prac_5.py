from cProfile import label
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# constants
e = np.e
R = 8.314 # J/mol-K
T_D = 215 # debye temp of copper
T_E = 151 # einsten temp of copper


def Dulong(T):
    return np.array(len(T)*[3*R])

def Einstein(T):
    '''
    Einstein heat capacity for a mole of any solid
    T: temprature at which to evaluate heat capacity
    '''
    C = 3*R*(T_E/T)**2
    C = C * ( e**( T_E/T ) ) / (e**( T_E/T ) - 1)**2
    return C

def Debye(T):
    '''
    Debye heat capacity for a mole of any solid
    T: temprature at which to evaluate heat capacity
    uses quadrature to eavluate integral
    '''
    f = lambda x :(x**4)*(e**x)/(e**x - 1)**2
    c_array = np.array([])
    # extract the value of integral
    for t in T:
        C = 9*R*(t/T_D)**3
        value = C*quad( f , 0.1 , T_D/t)[0]
        c_array = np.append(c_array,value)
   
    return c_array


# define temprature array
T_array = np.linspace(0.8,300,1000)

# store heat capacity 

# Dulong_Petit value 
C_DP  = Dulong(T_array)

# Einstein  Value
C_E = Einstein(T_array)

# Debye value
C_D = Debye(T_array)

plt.plot(T_array,C_DP,label='Dulong_Petit',ls=':')
plt.plot(T_array,C_E,label='Einstein',ls='--')
plt.plot(T_array,C_D,label='Debye')
plt.legend()
plt.title(r'$\theta_D = 215 K $ , $\theta_E = 151 K $ ')
plt.xlabel('Temperature (K)') 
plt.ylabel('Heat Capacity ( J / mol-K)')
plt.grid(True)
plt.show()
# print(Einstein(1))
# print(C_E)
# print(C_DP)
# print(C_E)

