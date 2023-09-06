import numpy as np
d = 2*np.pi/512

x = np.linspace(-np.pi, np.pi-d, 512)

y = np.linspace(-np.pi, np.pi-d, 512)

coordinates = [[xi, yi] for xi in x for yi in y]

coordinates1 = [[xi+1e-8, yi] for xi in x for yi in y]

print(coordinates[0:10])
print('/n')
print(coordinates1[0:10])