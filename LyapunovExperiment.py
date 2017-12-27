from math import *
from pylab import *
from numpy import *
from random import *

def derOmega(w,theta,t):
    #return -9.8*sin(theta)
    return -sin(theta)-w/2+1.2*sin(2*t/3)

def derTheta(w,theta,t):
    return w

def rkStep(w,theta,t):

    k1=dt*derOmega(w,theta,t)
    L1=dt*derTheta(w,theta,t)


    k2=dt*derOmega(w+k1/2,theta+L1/2,t+dt/2)
    L2=dt*derTheta(w+k1/2,theta+L1/2,t+dt/2)
    
    k3=dt*derOmega(w+k2/2,theta+L2/2,t+dt/2)
    L3=dt*derTheta(w+k2/2,theta+L2/2,t+dt/2)

    k4=dt*derOmega(w+k3,theta+L3,t+dt)
    L4=dt*derTheta(w+k3,theta+L3,t+dt)
    

    theta=theta+(L1+2*L2+2*L3+L4)/6
    w=w+(k1+2*k2+2*k3+k4)/6
    
    return w,theta



def plotGraph(w,theta,dt):
    t=0
    T=[]
    W=[]
    T.append(theta)
    W.append(w)
    for i in range (0, 150*(2**(8))):
        w,theta=rkStep(w,theta,t)
        W.append(w)
        T.append(theta)
        t+=dt
    t+=dt
    tPoints=arange(0,t,dt)
    return (T,W,tPoints)


dt=2**(-8)
T,W,tPoints=plotGraph(0,.2,dt)

T1,W1,tPoints=plotGraph(0,.2+(10**(-6)),dt)

dTheta=[]
for i in range (0, 150*(2**(8))+1):
    dTheta.append( log( abs( T1[i]-T[i]) ) )
plot(tPoints,dTheta,label="log of abs of Theta1-Theta2")
show()

delta=[]

for j in range(0,100):
    x=uniform(.2,.21)
    T,W,tPoints=plotGraph(0,x,dt)
    if(j==0):
        for i in range(0,150*2**(8)+1):
            delta.append(T[i])
    else:
        for i in range(0,150*2**(8)+1):
            delta[i]+=T[i]

for i in range(0,150*2**(8)+1):
    delta[i]=log(abs(delta[i]/100))


plot(tPoints,delta)

def line_best_fit(arrayX, arrayY):
    # Calculate the mean of x and y
    xbar = 0 
    for x in arrayX:
        xbar += x / len(arrayX)
    ybar = 0
    for y in arrayY:
        ybar += y / len(arrayY)
    # Calculate slope using least squares method
    m = xsum = 0
    for i in range( len(arrayX) ):
        m += (arrayX[i] - xbar)*(arrayY[i] - ybar)
        xsum += (arrayX[i] - xbar)**2
    m /= xsum
    # Plot the line of best fit
    b = ybar - m*xbar
    regression_line = []
    for x in arrayX:
        regression_line.append(m*x+b)
    return regression_line, m

lineS = 0    # Percentage into data to start best fit line
lineF = .05    # Percentage into data to finish best fit line
active = int(len(tPoints)*lineS), int(len(tPoints)*lineF)
best_fit, m = line_best_fit(tPoints[active[0]:active[1]], delta[active[0]:active[1]])
plot(tPoints[active[0]:active[1]], best_fit, label="Line of best fit", color='r')
legend(loc='lower right')
show()
print("The Lyapunov Exponent is approximately", m, "for this system.\n")
