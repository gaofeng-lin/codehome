# -*- coding: utf-8 -*-
import numpy as np
from differ import diff1d,diff2d
from sklearn.decomposition import PCA
from scipy.optimize import minimize
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

L = 4; N = 201;

x = np.linspace(-L/2, L/2, N).reshape(-1,1);
dx = x[1]-x[0]; 
dt = 2e-4
u = 0.75 * x + 0.5;
u_real = x**4/12 - x**3/6 + 17*x/12 - 5/6;
res_log = []

# O是模态数；这里没有论文里面提到的降维优化调用间隔C，或者说认为N*K=C
# 这个例子中，S有5列，用于存储流场快照
# u就是论文中的q0
N = 5; K = 100; O = 3;
C = N*K
S = np.zeros((u.shape[0], N))

# x shape : (201, 1)
# u shape : (201, 1)
# S shape : (201, 5)
print('x shape :', x.shape)
print('u shape :', u.shape)
print('S shape :', S.shape)


breakpoint()

for i in range(15000):
    
    res = Res(u)
    
    u = TimeMarching(u, res)
    
    u = Bondary(u)
    
    res_log.append(np.abs(res).mean())
    
    if i % K == K-1:
        S[:,[i//K%N]] = u       #Collect snapshots
    # 这个地方的N*K应该就是论文当中的C，也可以把N*K换成一个变量C，赋一个值
    # if i % (N*K) == N*K-1:
    #     u = DimensionReductionOpt(S)       #Call Dimension Reduction Optimization

    if i % C == C-1:
        u = DimensionReductionOpt(S)       #Call Dimension Reduction Optimization

plt.figure()
plt.plot(x, u); plt.plot(x, u_real, linestyle='dashed');
plt.figure()
plt.plot(np.log10(res_log))
plt.show()