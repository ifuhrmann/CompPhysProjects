from pylab import *
import numpy as np

M=100

Phi=np.zeros([M,M],float)
PhiP=np.zeros([M,M],float)

error=100
delta=10**(-6)

def rho(i,j):
    if(i<80 and i>60 and j<40 and j>20):
        return (1)
    if(j<80 and j>60 and i<40 and i>20):
        return (-1)
    else:
        return 0

while(error>delta):
    for i in range(0,M):
        for j in range(0,M):
            if(i==0 or j==0 or i==M-1 or j==M-1):
                PhiP[i][j]=Phi[i][j]
            else:
                PhiP[i][j]=(Phi[i+1][j]+Phi[i-1][j]+Phi[i][j+1]+Phi[i][j-1])/4+rho(i,j)/4
    error=np.max(np.abs(Phi-PhiP))
    Phi,PhiP=PhiP,Phi

imshow(Phi)
spectral()
show()
