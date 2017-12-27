from math import *
from pylab import *
from numpy import *
G=6.674*(10**(-11))
M=5.974*(10**(24))
m=7.348*(10**(22))
R=3.844*(10**(8))
w=2.662*(10**(-6))

r=R/4


def f(r):
    return (   G*M/(r**2) - G*m/((R-r)**2)-w*w*r  )

def fprime(r):
    return ( -G*2*M/(r**3) - G*2*m/((R-r)**3)-w*w  )



for i in range(0,10000):
    r=r-f(r)/fprime(r)
print("The lagrange point is",r/R,"% away from the earth")
