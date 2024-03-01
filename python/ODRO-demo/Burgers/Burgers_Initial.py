# -*- coding: utf-8 -*-
import numpy as np
from differ import diff1d,diff2d
from sklearn.decomposition import PCA
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def Res(u):
    du = - u*diff1d(u,[-1,0,1],1,1) / dx + 0.05*diff1d(u,[-1,0,1],2,1) / dx**2
    return du

def TimeMarching(u, res):
    u = u + res * dt
    return u

def Bondary(u):
    u[0] = 0.5; u[-1] = -0.5;
    return u

L = 2; N = 201;

x = np.linspace(-L/2, L/2, N).reshape(-1,1);
dx = x[1]-x[0]; dt = 5e-4
u = - 0.5 * x;

res_log = []

for i in range(30000):
    
    res = Res(u)
    
    u = TimeMarching(u, res)
    
    u = Bondary(u)
    
    res_log.append(np.abs(res).mean())

plt.figure()
plt.plot(x, u);
plt.figure()
plt.plot(np.log10(res_log))
plt.show()