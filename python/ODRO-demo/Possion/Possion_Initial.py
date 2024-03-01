# -*- coding: utf-8 -*-
import numpy as np
from differ import diff1d,diff2d
from sklearn.decomposition import PCA
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def Res(u):
    du = diff1d(u,[-1,0,1],2,1) / dx**2 - x**2 + x;
    return du

def TimeMarching(u, res):
    u = u + res * dt
    return u

def Bondary(u):
    u[0] = -1; u[-1] = 2;
    return u


L = 4; N = 201;

x = np.linspace(-L/2, L/2, N).reshape(-1,1);
dx = x[1]-x[0]; dt = 2e-4
u = 0.75 * x + 0.5;
u_real = x**4/12 - x**3/6 + 17*x/12 - 5/6;
res_log = []

for i in range(100000):
    
    res = Res(u)
    
    u = TimeMarching(u, res)
    
    u = Bondary(u)
    
    res_log.append(np.abs(res).mean())

plt.figure()
plt.plot(x, u); plt.plot(x, u_real, linestyle='dashed');
plt.figure()
plt.plot(np.log10(res_log))
plt.show()