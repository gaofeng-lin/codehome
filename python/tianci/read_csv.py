import pandas as pd
import torch

bc_data_path = 'C:\\openSouceCode\\codehome\\python\\tianci\\bc_data.csv'
x = torch.from_numpy(pd.read_csv(bc_data_path).values) 

print(x)