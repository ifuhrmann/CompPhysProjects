from math import *
from pylab import *
from numpy import *
 
#for approximating derivatives with (f(x+h)-f(x))/h set h to 10**-8
#because of limits of Python rounding
#try midpoint difference: f(x+h/2)-f(x-h/2)/h, h~c^1/3,e~c^2/3
#this puts h at about h = 10**-5

#there is always a way to write matrices as the product of
#a lower triangular and upper triangular matrix

# v1-v+  + v1-v3  +  v1-v4  +  v1-v2
# v1/r (-v+-v2-v3-v4)
