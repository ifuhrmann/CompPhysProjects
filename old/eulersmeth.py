from math import *
from pylab import *
from numpy import *

def der(x,t):
    return x

x0=1
t0=0
dt=2**(-24)
X=[]
X.append(x0)
j=0
for i in range (0,2**24):
    x0=x0+dt*der(x0,t0);
    t0+=dt
    X.append(x0)
    j+=1
print(x0,t0,j)
t0+=dt
tPoints=arange(0,t0,dt)
plot(tPoints,X)
show()
