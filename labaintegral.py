import numpy as np
from math import *
import pylab
from matplotlib import mlab


a = -3.0
b = 3.0
N = 60


F = 3.093362496096232

def f(x):
    return 1/(1+cos(x/5))


def rectangular(f, a, b, N):
    x = [0]*(N+1)
    result = [0]*(N+1)
    h = float(b - a)/N
    I=0
    for i in range(N+1):
        x[i] = a + h*i + h/2
    for i in range(N+1):
        result[i] = f(x[i])*h
        I+=result[i]
    return I

def trapezoidal(f, a, b, N):
    h = float(b - a)/N
    x = [0]*(N+1)
    result = [0]*(N+1)
    P=0.005
    for i in range(N+1):
        x[i] = a + h*i
    for i in range(N):
        result[i] =(f(x[i]) + f(x[i+1]))*h/2
        P+=result[i]
    return P

def sipson(f, a, b, N):
    h = float(b-a)/N
    x = [0]*(N+1)
    result = [0]*(N+1)
    P=0
    for i in range(N+1):
        x[i] = a + h*i
    if (N%2==0):
        for i in range(N):
            if i==N-2:
                result[i] = (f(b-h) + 4*f(b-h/2) + f(b))*h/6
            else:
                result[i] = (f(x[i-1]) + 4*f(x[i]) + f(x[i+1]))*h/6
            P+=result[i]
            i+=1
    else:
        for i in range(N):
            result[i] = (f(x[i-1]) + 4*f(x[i]) + f(x[i+1]))*h/6
            P+=result[i]
            i+=1
    return P



def graf(n):
    h=(b-a)/n
    x = [0]*(n+1)
    result = [0]*(n+1)
    pog = 0
    P=0
    for i in range(n+1):
        x[i] = a + h*i
    if(n%2==0):
        for i in range(n):
            if i==n-2:
                result[i] = (f(b-h) + 4*f(b-h/2) + f(b))*h/6
            else:
                result[i] = (f(x[i-1]) + 4*f(x[i]) + f(x[i+1]))*h/6
            P+=result[i]
            i+=1
    else:
        for i in range(n):
            result[i] = (f(x[i-1]) + 4*f(x[i]) + f(x[i+1]))*h/6
            P+=result[i]
            i+=1
    pog = (abs(F-P))
    return(log(pog)) 



F1 = rectangular(f, a, b, N)
F2 = trapezoidal(f, a, b, N)
print(abs(F - F1))
print('\n')
print(F1)
print('\n\n\n')
print(abs(F - F2))
print('\n')
print(F2)
print('\n\n\n')
F3 = sipson(f, a, b, N)
print(abs(F - F3))
print('\n')
print(F3)
print('\n\n\n')
print('\n\n\n')

xlist = [0]*(10)
ylist = [0]*(10)

for i in range(1,11):
    ylist[i-1] = abs(graf(i*20))

for i in range(1,11):
    xlist[i-1] = abs(log(i*20))
    k=0

for i in range(1,9):
    k = (ylist[i+1]-ylist[i])/(xlist[i+1]-xlist[i]) + k
print('Коэффициент угла наклона прямой k =',k/4)

pylab.grid(True)
pylab.plot(xlist,ylist,'o',xlist,ylist)
pylab.show()


"""F1 = rectangular(f, a, b, N)
F2 = trapezoidal(f, a, b, N)
F3 = sipson(f, a, b, N)
print(abs(F - F1))
print('\n')
print(F1)
print('\n\n\n')
print(abs(F - F2))
print('\n')
print(F2)
"""


