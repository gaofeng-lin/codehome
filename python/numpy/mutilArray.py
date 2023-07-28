#coding=UTF-8

import numpy as np

a=np.random.randint(0,10,size=[3,3,3,3])
 
b = a[1]
c = a[1][:,1:2,1:2]
print ('a :',a)
print('b :',b)
print('c :',c)