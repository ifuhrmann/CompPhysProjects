from math import *
from pylab import *
from numpy import *
from random import *

def derOmega(w,theta,t):
    return -sin(theta)

def derTheta(w,theta,t):
    return w

def rkStep(w,theta,t):

    k1=dt*derOmega(w,theta,t)
    L1=dt*derTheta(w,theta,t)


    k2=dt*derOmega(w+k1/2,theta+L1/2,t+dt/2)
    L2=dt*derTheta(w+k1/2,theta+L1/2,t+dt/2)
        

    w=w+k1
    theta=theta+L2

    return w,theta



def plotGraph(w,theta,dt):
    t=0
    T=[]
    W=[]
    E=[]
    T.append(theta)
    W.append(w)
    E.append((w*w*9.8*9.8-9.8*9.8*cos(theta))/2)
    for i in range (0, 150*(2**(8))):
        w,theta=rkStep(w,theta,t)
        W.append(w)
        T.append(theta)
        E.append((.5*w*w*9.8*9.8-9.8*9.8*cos(theta))/2)
        t+=dt
    t+=dt
    tPoints=arange(0,t,dt)
    return (T,W,tPoints,E)


dt=2**(-8)
T,W,tPoints,E=plotGraph(0,.2,dt)

T1,W1,tPoints,E=plotGraph(0,.2+(10**(-6)),dt)



plot(tPoints,E)
show()

