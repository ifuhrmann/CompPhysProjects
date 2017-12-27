from pylab import *
import numpy as np

V=1
M=100

Phi=np.zeros([M,M],float)
PhiP=np.zeros([M,M],float)

Phi[0,:]=V
error=100
delta=10**(-3)



while(error>delta):
    for i in range(0,M):
        for j in range(0,M):
            if(i==0 or j==0 or i==M-1 or j==M-1):
                PhiP[i][j]=Phi[i][j]
            else:
                PhiP[i][j]=(Phi[i+1][j]+Phi[i-1][j]+Phi[i][j+1]+Phi[i][j-1])/4
    error=np.max(np.abs(Phi-PhiP))
    Phi,PhiP=PhiP,Phi

imshow(Phi)
spectral()
show()
