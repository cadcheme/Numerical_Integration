from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

#Data 
Ca0 = 42
Cb0 = 30
Cc0 = 4
K = 0.015

xguess = np.linspace(0,10,11)
zstore = np.zeros(len(xguess))

def myfun(X,Ca0,Cb0,Cc0,K):
    Ca = Ca0 - 2*X
    Cb = Cb0 - X
    Cc = Cc0 + X
    F = K - Cc/(Ca**2*Cb) 
    return F

for i in range(0, len(xguess)):
    x = xguess[i]
    z = quad(myfun, 0, x, args=(Ca0,Cb0,Cc0,K))
    zstore[i] = z[0]
    
plt.plot(x,zstore)