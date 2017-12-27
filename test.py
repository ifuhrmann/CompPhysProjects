from math import *
#these are comments now
from numpy import *
from pylab import plot,show
# import works in 2.7.12 but not 3.6

def f(x):
    return(exp(-(x**2)/2))
n=int(input("How many intervals?"))
r=[]
for z in range(0,100):
    y=z
    h=(y-0)/n
    x=0
    total=0
    for d in range(1,n):
       total+=(2+2*(d%2))*f(x+d*h)
    total+=(f(0)+f(y))
    total*=(h/3)
    r.append(total)
    print(total)
l=linspace(0,100,100)
plot(l,r)
show()


#savetxt('filename.txt',x) saves array x to file 
#loadtxt('filename.txt') loads array from file
#can specify file path in filename
#by the way these are in numpy
#x[1][2:4] gives an array of the indices of x[1] from 2 to 3
