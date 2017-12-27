from math import *
from pylab import *
from numpy import *


def derOmega(w,theta,t):
    return -sin(theta)-w/2+1.465*sin(2*t/3)

def derTheta(w,theta,t):
    return w

def rkStep(w,theta,t):

    k1=dt*derOmega(w,theta,t)
    L1=dt*derTheta(w,theta,t)


    k2=dt*derOmega(w+k1/2,theta+L1/2,t+dt/2)
    L2=dt*derTheta(w+k1/2,theta+L1/2,t+dt/2)
    
    k3=dt*derOmega(w+k2/2,theta+L2/2,t+dt/2)
    L3=dt*derTheta(w+k2/2,theta+L2/2,t+dt/2)

    k4=dt*derOmega(w+k3,theta+L3,t+dt)
    L4=dt*derTheta(w+k3,theta+L3,t+dt)
    

    theta=theta+(L1+2*L2+2*L3+L4)/6
    w=w+(k1+2*k2+2*k3+k4)/6
    
    return w,theta



def plotGraph(w,theta,dt):
    t=0
    T=[]
    W=[]
    T.append(theta)
    W.append(w)
    for i in range (0, 1000*(2**(8))):
        w,theta=rkStep(w,theta,t)
        if(theta<-pi):
            theta+=2*pi
        if(theta>pi):
            theta-=2*pi
        if(t>2000):
            if(abs(w*t/(2*pi)-floor(w*t/(2*pi)))<(dt/100)):
                Tp.append(theta)
                Wp.append(w)
        W.append(w)
        T.append(theta)
        t+=dt
    t+=dt
    tPoints=arange(0,t,dt)
    return (T,W,tPoints)


dt=2**(-8)
Tp=[]
Wp=[]

#T,W,tPoints=plotGraph(0,.2,dt)
#plot(Tp,Wp,"k.")
#show()

T,W,tPoints=plotGraph(0,.2,dt)
plot(tPoints,T)
show()
