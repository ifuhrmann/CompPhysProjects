from math import *
import numpy as np
import pylab as pl
from random import random, randrange


i=0
N=100
S=np.zeros([N,N],bool)
J = 1
step = 200000


def eandm(T):
    E = -2*N*N       # Energy of our system
    M = N*N
    eMeasured = 0
    mMeasured = 0
    countM = 0
    S = np.ones([N,N], float)
    for i in range(step):
        k1 = randrange(N)
        k2 = randrange(N)
        dE = 2*J*S[k1,k2]*(S[(k1-1)%N, k2] + S[(k1+1)%N, k2] + S[k1, (k2-1)%N] + S[k1, (k2+1)%N])
        R = np.e**(-dE/T)
        if (R > 1 or random() < R):
            S[k1, k2] = -S[k1, k2]
            E += dE
            M += 2*S[k1,k2]
        if i > 20000 and i % N*N == 0:
            eMeasured += E
            mMeasured += np.abs(M)
            countM += 1
    return eMeasured / countM, mMeasured / countM




ePts = []
mPts = []
Temp = np.arange(0.1, 4, 0.1)
for t in Temp:
    var = eandm(t)
    ePts.append(var[0])
    mPts.append(var[1])

pl.plot(Temp, ePts, label="E")
pl.plot(Temp, mPts, label="M")
pl.legend()
pl.show()

eDer=[]
mDer=[]
for i in range(len(ePts)-1):
    eDer.append((ePts[i+1]-ePts[i])/.1)
    mDer.append((mPts[i+1]-mPts[i])/.1)
eDer.append((ePts[len(ePts)-1]-ePts[len(ePts)-2])/.1)
mDer.append((mPts[len(ePts)-1]-mPts[len(ePts)-2])/.1)
pl.plot(Temp,eDer)
pl.plot(Temp,mDer)
pl.show()
    

