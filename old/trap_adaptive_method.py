from math import *
from pylab import plot,show
from numpy import *
def f(x):
    return((1/(1-x)**2)*e**(-(x/(1-x))**2))
n=int(input("How many intervals?"))
y=int(input("How far?"))
h=(y-0)/n
x=0
total=0
delta=10**-13
for d in range(1,n):
   total+=h*f(x+d*h-delta)
total+=h*f(0)/2
total+=h*f(y-delta)/2
print(total)

error=10
told=total
while(error>delta):
    told=total
    h=h/2
    n=2*n
    total=total/2
    for d in range(1,n,2):
        total+=h*f(x+d*h-delta)
    error=abs((total-told)/3)
    print(total,error)

# integral from 0 to infinity of f(x)dx
# == to the integral from 0 to 1 of f(z/1-z) times dz/(1-z)^z
#for the integral from a to infinity go to
#the integral of f(z/1-z  +a) times dz/(1-z)^2
#for the integral from -inf to inf, we do it im two parts
#0 to inf, -inf to 0, with the same change of variable trick   
#
#
#doing double integrals:
#
#
