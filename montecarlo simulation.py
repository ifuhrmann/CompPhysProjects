from math import *
from pylab import *
from numpy import *
from random import *




tot=0
X=[]
for i in range(1000000):
    x=random()**2
    tot+=2/(e**(x)+1)
tot=tot/1000000
print(tot)
