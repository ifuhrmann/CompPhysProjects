from math import *
from pylab import *
from numpy import *



sigma=10
r=28
b=8/3

def dx(x,y,z):
    return(sigma*(y-x))
def dy(x,y,z):
    return(r*x-y-x*z)
def dz(x,y,z):
    return(x*y-b*z)


def rkStep(x,y,z,t):
    k1=dt*dx(x,y,z)
    L1=dt*dy(x,y,z)
    M1=dt*dz(x,y,z)
    
    k2=dt*dx(x+k1/2,y+L1/2,z+M1/2)
    L2=dt*dy(x+k1/2,y+L1/2,z+M1/2)
    M2=dt*dz(x+k1/2,y+L1/2,z+M1/2)

    k3=dt*dx(x+k2/2,y+L2/2,z+M2/2)
    L3=dt*dy(x+k2/2,y+L2/2,z+M2/2)
    M3=dt*dz(x+k2/2,y+L2/2,z+M2/2)

    k4=dt*dx(x+k3,y+L3,z+M3)
    L4=dt*dy(x+k3,y+L3,z+M3)
    M4=dt*dz(x+k3,y+L3,z+M3)

    
    x+=(k1+2*k2+2*k3+k4)/6
    y=y+(L1+2*L2+2*L3+L4)/6
    z=z+(M1+2*M2+2*M3+M4)/6

    return x,y,z

x=0
y=1
z=0
t=0
dt=2**(-10)
X=[x]
Y=[y]
Z=[z]
for i in range(0, 100*2**(10)):
    x,y,z=rkStep(x,y,z,t)
    X.append(x)
    Y.append(y)
    Z.append(z)
    t+=dt
t+=dt
tPoints=arange(0,t,dt)
plot(Y,tPoints)
show()

plot(X,Z)
show()
    
