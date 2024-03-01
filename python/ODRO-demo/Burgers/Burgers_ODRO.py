# -*- coding: utf-8 -*-
import numpy as np
from differ import diff1d,diff2d
from sklearn.decomposition import PCA
from scipy.optimize import minimize
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

def DimensionReductionOpt(S):
    #POD analysis
    pca = PCA(n_components=O)
    coeff = pca.fit_transform(S.T)
    
    u_mean = pca.mean_.reshape(-1,1)
    u_modes = pca.components_.T
    # a0 = coeff[[-1]]
    a0 = coeff[-1] 
    
    #Optimization
    def Obj(a):
        u = u_mean + u_modes@(a.reshape(-1,1))
        res = Res(u)
        obj = np.abs(res).mean()
        return obj
    outputs = minimize(Obj, a0, method='Nelder-Mead',tol=1e-16,options={'maxiter': int(N*K/10)})
    
    u = u_mean + u_modes@(outputs.x.reshape(-1,1))
    return u

L = 2; N = 201;

x = np.linspace(-L/2, L/2, N).reshape(-1,1);
dx = x[1]-x[0]; dt = 5e-4
u = - 0.5 * x;

res_log = []


N = 5; K = 100; O = 3;
S = np.zeros((u.shape[0], N))

for i in range(10000):
    
    res = Res(u)
    
    u = TimeMarching(u, res)
    
    u = Bondary(u)
    
    res_log.append(np.abs(res).mean())
    
    if i % K == K-1:
        S[:,[i//K%N]] = u       #Collect snapshots
    if i % (N*K) == N*K-1:
        u = DimensionReductionOpt(S)       #Call Dimension Reduction Optimization

plt.figure()
plt.plot(x, u);
plt.figure()
plt.plot(np.log10(res_log))
plt.show()