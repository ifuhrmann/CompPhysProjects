from math import *
from pylab import plot,show
from numpy import *
from numpy.linalg import eigh
A=array([[1,2],[2,4]])
print(A)
print(eigh(A))

E=[]

hbar=6.6*(10**-34)/(2*pi)
m_e=9.1*(10**-31)
L=5*(10**-10)
e=1.6*(10**-19)
for i in range(1,11):
    E.append(  i*i*pi*pi*(hbar**2)/(2*m_e*(L**2)) )
print(E)

def V_x(x):
    return(10*e*x/L)

def Hphi(x,n,m):
    total=((hbar**2)*(1/(2*m_e))*((n*pi/L)**2)*(sin(n*pi*x/L)))
    total+=sin(n*pi*x/L)*V_x(x)
    total*=(2/L)*sin(m*pi*x/L)
    return total
def simpson(x,y,n,m,f=lambda x:1):
    n1=100
    h=(y-x)/n1
    total=0
    for d in range(1,n1):
        total+=(2+2*(d%2))*f(x+d*h,n,m)
    total+=(f(x,n,m)+f(y,n,m))
    total*=(h/3)
    return(total)

print(Hphi(1,1,1))
print(simpson(0,L,1,2,Hphi))
A=zeros([10,10])
for n in range(1,11):
    for m in range(1,11):
        A[n-1,m-1]=simpson(0,L,n,m,Hphi)
print(A)
B,C=eigh(A)
print("\n")
B=list(map(lambda x:x/e,B))
print(B)
#print(C)
