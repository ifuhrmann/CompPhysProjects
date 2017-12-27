from math import *
from pylab import *
from numpy import *

def B(x,y,z):
    s=0
    a=0
    b=2*pi
    h=.1
    n=int((b-a)/h)
    r=array([x,y,z])
    for i in range(1,n):
        r1=array([x-3*cos(i*h),y-2*sin(i*h),z])
        s+=(2+2*(i%2))*cross(r,r1)/(( (x-3*cos(i*h))**2+(y-2*sin(i*h))**2+(z)**2)**(3/2))
    r1=array([x-3,y,z])
    s+=cross(r,r1)/(( (x-3*cos(0))**2+(y-2*sin(0))**2+(z)**2)**(3/2))
    s+=cross(r,r1)/(( (x-3*cos(2*pi))**2+(y-2*sin(2*pi))**2+(z)**2)**(3/2))
    return ((h/3)*(s))

print(B(1,4,7))


def B_trap(x,y,z):
    s=0
    a=0
    b=2*pi
    n=10
    h=(b-a)/n
    r=array([x,y,z])
    def f(theta):
        r1=array([x-3*cos(i*h),y-2*sin(i*h),z])
        return(cross(r,r1)/(( (x-3*cos(i*h))**2+(y-2*sin(i*h))**2+(z)**2)**(3/2)))
    for i in range(1,n):
        s+=f(i*h)
    s+=f(a)/2
    s+=f(b)/2
    s*=h
    error=10
    told=s
    while(error>10**-6):
        told=s
        h=h/2
        n=2*n
        s=s/2
        for i in range(1,n,2):
            s+=h*f(a+i*h)
        e=(s-told)/3
        error=sqrt(e.dot(e))
    return (s)


print(B_trap(1,2,5))

points = 100

arr = empty([points, points], float)
for i in range(0, points):
    y = (i-50)/10
    for j in range(0, points):
        x = (j-50)/10
        t=B(x,y,1)
        arr[i,j] = sqrt(t.dot(t))

print("here")

imshow(arr, origin="lower", extent=[-5,5,-5,5])
bone() 
show()
