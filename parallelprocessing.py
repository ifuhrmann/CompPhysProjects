import multiprocessing,time
from math import *
from pylab import *
from numpy import *


def f(x):
    return( e**(-(x**2)))

def I(xmax):
    step=.001
    s=0
    s+=f(0)*step
    count=int(xmax/step)
    for i in range(count):
        s+=f(0+(i*step))*step
    return s


if __name__=='__main__':
    print(multiprocessing.cpu_count())
    t=time.time()
    x_entries=arange(0,10,.001)
    cores=multiprocessing.Pool()
    results=cores.map(I,x_entries)
    cores.close()
    cores.join()
    plot(x_entries,results)
    print("This took {} seconds".format(time.time()-t))
    show()
