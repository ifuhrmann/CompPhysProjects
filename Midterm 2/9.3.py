from pylab import *
import numpy as np

M=100

Phi=np.zeros([M,M],float)
PhiP=np.zeros([M,M],float)

error=100
delta=10**(-6)


while(error>delta):
    for i in range(0,M):
        for j in range(0,M):
            if(i==0 or j==0 or i==M-1 or j==M-1):
                PhiP[i][j]=Phi[i][j]
            elif( (j==20 and i>=20 and i<=80) ):
                Phi[i][j]=1
            elif( (j==80 and i>=20 and i<=80) ):
                Phi[i][j]=-1
            else:
                PhiP[i][j]=(Phi[i+1][j]+Phi[i-1][j]+Phi[i][j+1]+Phi[i][j-1])/4
    error=np.max(np.abs(Phi-PhiP))
    Phi,PhiP=PhiP,Phi

imshow(Phi)
spectral()
show()
