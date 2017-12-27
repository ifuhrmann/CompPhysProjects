from math import *
from pylab import *
from numpy import *
#constants
m=9.1094*(10**(-31))
hbar=1.0546*(10**(-34))
e=1.6022*(10**(-19))
a=10**(-11)
L=20*a
N=1000
h=L/N
V0=50*e

def V(x):
    return V0*(x*x*x*x/(a**4))

def f(r,x,E):
    psi=r[0]
    phi=r[1]
    fpsi=phi
    fphi=(2*m/((hbar)**2))*(V(x)-E)*psi
    return array([fpsi,fphi],float)

def solve(E):
    psi=-10*a
    phi=1.0
    r=array([psi,phi],float)

    for x in arange(-10*a,10*a,h):
        k1=h*f(r,x,E)
        k2=h*f(r+.5*k1,x+h/2.0,E)
        k3=h*f(r+.5*k2,x+h/2.0,E)
        k4=h*f(r+k3,x+h,E)
        r+=(k1+2*k2+2*k3+k4)/6
    return(r[0])



def findE(E2):
    E1=0.0
    psi2=solve(E1)
    target = e/100000
    while abs(E1-E2)>target:
        psi1,psi2=psi2,solve(E2)
        E1,E2=E2,E2-psi2*(E2-E1)/(psi2-psi1)
    print("E =",E2/e,"eV")
    return E2


def graph(E):
    psi=0
    phi=1.0
    r=array([psi,phi],float)
    Psi=[psi]
    for x in arange(-10*a,10*a,h):
        k1=h*f(r,x,E)
        k2=h*f(r+.5*k1,x+h/2.0,E)
        k3=h*f(r+.5*k2,x+h/2.0,E)
        k4=h*f(r+k3,x+h,E)
        r+=(k1+2*k2+2*k3+k4)/6
        Psi.append(r[0])
    return(Psi,arange(-10*a,10*a+h,h))

def trapInt(F,X):
    total=0
    for i in range(1,size(X)-201):
        total+=h*(F[i]*F[i])
    total+=F[0]/2+F[size(X)-201]/2
    return 1/total

E=findE(e/100)
Psi,X=graph(E)
c=trapInt(Psi,X)
for i in range(0,size(Psi)):
    Psi[i]=c*Psi[i]
plot(X[250:size(X)-250],Psi[250:size(Psi)-250])

E1=findE(400*e)
Psi1,X1=graph(E1)
c=trapInt(Psi1,X1)
for i in range(0,size(Psi1)):
    Psi1[i]=c*Psi1[i]
plot(X1[250:size(X1)-250],Psi1[250:size(Psi1)-250])


E2=findE(1000*e)
Psi2,X2=graph(E2)
c=trapInt(Psi2,X2)
for i in range(0,size(Psi2)):
    Psi2[i]=c*Psi2[i]
plot(X2[250:size(X1)-250],Psi2[250:size(Psi2)-250])


show()


