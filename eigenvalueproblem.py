from math import *
from pylab import *
from numpy import *



def dv(v,x,t):
    return -9.8
def dx(v,x,t):
    return(v)

def rkStep(x,v,t,dt):

    k1=dt*dv(v,x,t)
    L1=dt*dx(v,x,t)


    k2=dt*dv(v+k1/2,x+L1/2,t+dt/2)
    L2=dt*dx(v+k1/2,x+L1/2,t+dt/2)
    
    k3=dt*dv(v+k2/2,x+L2/2,t+dt/2)
    L3=dt*dx(v+k2/2,x+L2/2,t+dt/2)

    k4=dt*dv(v+k3,x+L3,t+dt)
    L4=dt*dx(v+k3,x+L3,t+dt)
    

    x=x+(L1+2*L2+2*L3+L4)/6
    v=v+(k1+2*k2+2*k3+k4)/6
    
    return x,v



def f(v):
    x=0
    dt=2**(-8)
    t=0
    for i in range (0, 10*(2**(8))):
        x,v=rkStep(x,v,t,dt)
        t+=dt
    t+=dt
    tPoints=arange(0,t,dt)
    return (x)



v1=100
v2=-100
error=100
d=10**(-8)


while error > d:
    vp= (v1+v2)/2
    if(f(vp)*f(v1)>0):
        v1=vp
    else:
        v2=vp
    error=abs(f(v2)-f(v1))
    
print((v1+v2)/2)
