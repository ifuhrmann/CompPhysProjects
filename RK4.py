from math import *
from pylab import *
from numpy import *

def der(x,t):
    return -x**3+sin(t)

def rkStep(x,t,der=lambda x,t:1):
    k1=der(x,t)
    k2=der(x+dt*k1/2,t+dt/2)
    k3=der(x+dt*k2/2,t+dt/2)
    k4=der(x+dt*k3,t+dt)
    x=x+dt*(k1+2*k2+2*k3+k4)/6
    return x

x=1
t=0
dt=2**(-12)
X=[]
X.append(x)
j=0
for i in range (0,10 * 2**12):
    x=rkStep(x,t,der)
    X.append(x)
    t+=dt
    j+=1
print(x,t,j)
t+=dt
tPoints=arange(0,t,dt)
plot(tPoints,X,label="RK")
legend()
show()

