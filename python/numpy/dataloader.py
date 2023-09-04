import numpy as np
import torch
from torch.utils.data import DataLoader 

pde = torch.randn(10, 3)

pde_xs = [pde[:, i:i+1] for i in range(3)]

print(pde_xs)

zip_pde = zip(*pde_xs)
list_pde  = list(zip_pde)

print('zip_pde: ',zip_pde)
print('list_pde: ',list_pde)

# pde_loader = DataLoader(list(zip(*pde_xs)), batch_size=5)

# for i, data in enumerate(pde_loader):
#     print('data:{0} '.format(data))
