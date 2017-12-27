from math import *
from pylab import *
from numpy import *

def derOmega(w,theta,t):
    #return -9.8*sin(theta)
    return -sin(theta)

def derTheta(w,theta,t):
    return w



def plotGraph(w,theta,dt):
    t=0
    T=[]
    W=[]
    T.append(theta)
    W.append(w)
    
    wHalf=w+dt*derOmega(w,theta,t)
    thetaHalf=theta+dt*derTheta(w,theta,t)
    
    for i in range (0, 150*(2**(8))):
        
        w+=dt*derOmega(wHalf,thetaHalf,t+dt/2)
        theta+=dt*derTheta(wHalf,thetaHalf,t+dt/2)
        
        wHalf+=dt*derOmega(w,t,t+dt)
        thetaHalf+=dt*derTheta(w,t,t+dt)

        W.append(w)
        T.append(theta)

        t+=dt
    t+=dt
    tPoints=arange(0,t,dt)
    return (T,W,tPoints)

T,W,t=plotGraph(0,.2,2**(-8))
plot(T,W)
show()
