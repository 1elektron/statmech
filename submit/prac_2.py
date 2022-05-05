'''
This program calulates probablity of different outcomes of N coint tosses.
'''

import math
import matplotlib.pyplot as plt


# N is total number if coins
N = 16

# total multiplicity, omegaT is toal number of microsates 
# N coins can have
omegaT = 2**N


# multiplicity of n heads, is the number of ways n head
# can show up on toss of N coins. The list stores that value 
# for n ranging to no head(=0) to all head(=N)
omega_n = [math.comb(N,n) for n in range(N+1)]

# TO calulate probability of n head,just divide multiplicty of 
# n head by total multiplicity
probability_n = [math.comb(N,n)/omegaT for n in range(N+1)]

# Plot
plt.grid(True)         
plt.bar([n for n in range(N+1)],probability_n)
plt.title('Number of coins=%i'%N)  
plt.xticks([n for n in range(N+1)])
                                       
plt.xlabel("Number of Heads")                                                      
plt.ylabel(" Probability ")                                                                                       
plt.show()
