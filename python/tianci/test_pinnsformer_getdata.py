import numpy as np

def get_data(x_range, y_range, x_num, y_num):
    x = np.linspace(x_range[0], x_range[1], x_num)
    t = np.linspace(y_range[0], y_range[1], y_num)

    x_mesh, t_mesh = np.meshgrid(x,t)
    data = np.concatenate((np.expand_dims(x_mesh, -1), np.expand_dims(t_mesh, -1)), axis=-1)
    print('data is : ', data)

    b_left = data[0,:,:] 
    b_right = data[-1,:,:]
    b_upper = data[:,-1,:]
    b_lower = data[:,0,:]
    res = data.reshape(-1,2)

    return res, b_left, b_right, b_upper, b_lower

res, b_left, b_right, b_upper, b_lower = get_data([-np.pi, np.pi], [0, 1], 51, 51)

print('res is : ', res)
print('b_left is : ', b_left)
print('b_right is : ', b_right)
print('b_upper is : ', b_upper)
print('b_lower is : ', b_lower)