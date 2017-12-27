from math import *
from pylab import *
from numpy import *
from random import * #random,randrange

sig=1
X=[]
Y=[]
for i in range(10000):
    theta=random()*2*pi
    r=sqrt(-2*sig*sig*log(1-random()))
    x=r*cos(theta)
    y=r*sin(theta)
    X.append(x)
    Y.append(y)
plot(X,"k.")
show()
