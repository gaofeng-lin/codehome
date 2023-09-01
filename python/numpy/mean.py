import numpy as np
import torch

x = [
[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
[[13,14,15,16],[17,18,19,20],[21,22,23,24]]
]
x = torch.tensor(x).float()
#
print("shape of x:")  ##[2,3,4]                                                                      
print(x.shape)                                                                                   
#
print("shape of x.mean(axis=0,keepdim=True):")          #[1, 3, 4]
print(x.mean(axis=0,keepdim=True).shape)       
print(x.mean(axis=0,keepdim=True))                 
#
# print("shape of x.mean(axis=0,keepdim=False):")         #[3, 4]
# print(x.mean(axis=0,keepdim=False).shape)     
# print(x.mean(axis=0,keepdim=False))                 
# #
print("shape of x.mean(axis=1,keepdim=True):")          #[2, 1, 4]
print(x.mean(axis=1,keepdim=True).shape)    
print(x.mean(axis=1,keepdim=True))                    
# #
# print("shape of x.mean(axis=1,keepdim=False):")         #[2, 4]
# print(x.mean(axis=1,keepdim=False).shape)                    
# #
print("shape of x.mean(axis=2,keepdim=True):")          #[2, 3, 1]
print(x.mean(axis=2,keepdim=True).shape)    
print(x.mean(axis=2,keepdim=True))                    
# #
# print("shape of x.mean(axis=2,keepdim=False):")         #[2, 3]
# print(x.mean(axis=2,keepdim=False).shape)                  
