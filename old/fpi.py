from math import *
from pylab import plot,show
from numpy import *
x=.5
temp=1
delta=10
def f(x):
    return(sqrt(1+log(x)))
while(delta>10**(-10)):
    temp=x
    x=f(x)
    delta=abs(temp-x)
    print(x,delta)
    
