from math import *
from random import *

def getVol(d):
    t=0
    for i in range(100000):
        s=0
        for ij in range(0,d):
            x=random()*2-1
            s+=x*x
        s=sqrt(s)
        if(s<=1):
            t+=1
    print((2**(d))*t/100000,d)
for i in range(1,12):
    getVol(i)
