from math import *
from pylab import *
from numpy import *
from random import * #random,randrange
seed=1
a=1664525
c=1013904223
n=4294967296
X=[]
Y=[]
x=seed
for i in range(0,200):
    x=(a*x+c)%n
    X.append(i)
    Y.append(x)
plot(Y,"k.")
show()

