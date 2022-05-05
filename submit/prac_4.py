import numpy as np
import matplotlib.pyplot as plt

#constants actual

h = 6.626*(10**(-34)) # J-s
k = 1.381*10**(-23) # J/K
m = 32*1.66*10**(-27) # kg
pi= np.pi
e = np.e
T1 = 200 # K
T2 = 300 # K
T3 = 600 # K

def maxwell_speed_dist(v,T):
    ''' 
    v : speed
    T: temprature
    '''
    v0 = 4*pi*np.power( (m / (2*pi*k*T) ) ,3/2)
    return v0 * (v**2) *  e**( -m*(v**2)/(2*k*T) )

def integrate_n_sort(x,y):
    '''
    Intergrate and sort
    x : array of x values, not used here
    y : array of y values, to be integrated

    '''
    dx = x[1]-x[0]
    y_avg = 0 
    y_sq_avg = 0
    j=0
    y_new = 0
    y_max = 0
    max_at = 0 # store the index at whihc y is max
    for i in y:
        y_avg = y_avg + x[j]*i*dx
        y_sq_avg = y_sq_avg + (x[j]**2)*i*dx

        y_new=  i
        if(y_new>y_max):
            y_max=y_new
            max_at = j
        
        j += 1
    v_max = x[max_at]
    y_rms = np.sqrt(y_sq_avg)

    return y_avg,y_rms,v_max,max_at


# Calculate arrays
v_array = np.linspace(0,2000,200)
f_2 = maxwell_speed_dist( v_array,T2) # dist of speed
f_3 = maxwell_speed_dist( v_array,T3) # dist of speed

# find avg, rms and max velocity
v_avg , v_rms ,v_max , i = integrate_n_sort(v_array,f_2)
print('At T = 300K')
print('v_avg = ', round(v_avg,3),'v_rms=',round(v_rms,3),'v_max=',round(v_max,3))

v_avg , v_rms ,v_max , i = integrate_n_sort(v_array,f_3)
print('At T = 600K')
print('v_avg = ', round(v_avg,3),'v_rms=',round(v_rms,3),'v_max=',round(v_max,3))

eqn = r'$ \left( \frac{m}{2\pi k_B T} \right)^{3/2} 4 \pi v^2 e^{-mv^2/k_B T} $'
# plt.text()
#plot
plt.plot( v_array, f_2  ,label='300K')
plt.plot( v_array, f_3  ,label='600K')

plt.xlabel(r'Speed $(m/s)$',fontsize=14)
plt.ylabel(r'Probablity Density $(s/m)$',fontsize=14)
plt.title(r'Maxwell Speed Dist.  $\left( \frac{m}{2\pi k_B T} \right)^{3/2} 4 \pi v^2 e^{-mv^2/k_B T}$ for $O_2$ ',fontsize=16)
plt.grid(True,ls='--')
plt.legend(fontsize=14)
plt.show()