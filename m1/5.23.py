from math import *
from pylab import *
from numpy import *
from numpy import loadtxt
data = loadtxt('altitude.txt')  # loads the data file
def dWdx(x,y):
    if(x!=511):
        return((data[x+1][y]-data[x][y])/30000)
    else:
        return((data[x][y]-data[x-1][y])/30000)

def dWdy(x,y):
    if(y!=1023):
        return((data[x][y+1]-data[x][y])/30000)
    else:
        return((data[x][y]-data[x][y-1])/30000)


arr = empty([512, 1024], float)
for i in range(0, 512):
    for j in range(0, 1024):
        arr[i,j] = (dWdx(i,j)+dWdy(i,j))/(sqrt(2)*sqrt(dWdx(i,j)**2+dWdy(i,j)**2+1))


imshow(arr)
bone() 
show()



def dHdx(x,y):
    if(x!=662):
        return((data[x+1][y]-data[x][y])/2.5)
    else:
        return((data[x][y]-data[x-1][y])/2.5)

def dHdy(x,y):
    if(y!=675):
        return((data[x][y+1]-data[x][y])/2.5)
    else:
        return((data[x][y]-data[x][y-1])/2.5)

data = loadtxt('stm.txt')  # loads the data file

arr = empty([663, 676], float)
for i in range(0, 663):
    for j in range(0, 676):
        arr[i,j] = (dHdx(i,j)+dHdy(i,j))/(sqrt(2)*sqrt(dHdx(i,j)**2+dHdy(i,j)**2+1))

imshow(arr)
bone() 
show()


