# 这段代码是从原始数据当中把值小于-e4的数据选出来，按照ux,uy,p分类。

import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay, distance
from collections import defaultdict
from shapely.geometry import Polygon
# import shapely


def PlotData(data):
    unique_t_values = np.unique(data[:, 2])

    for t in unique_t_values:
        subset = data[data[:, 2] == t]

        x = subset[:, 0]
        y = subset[:, 1]
        p = subset[:, 3]

        plt.figure()
        plt.scatter(x, y, c=p, cmap='viridis')  # 使用p值为颜色
        plt.colorbar(label='p value')
        plt.title(f"Data for t={t}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


def FilteredData(data):
    filtered_data = data[ (data[:, 3] > -9e-4) & (data[:, 3] < 0)]
    return filtered_data

def generate():
    # f = h5py.File('./Data_16.h5', 'r')
    f = h5py.File('C:\\Competition\\baseline_v2\\data_16.h5', 'r')
    n_frame = len(f.keys())
    XYT = np.zeros((0,3))
    UX = np.zeros((0,1))
    UY = np.zeros((0,1))
    P = np.zeros((0,1))
    for key in f.keys():
        time = float(key)
        XY = f[key][:,0:2]
        ux = f[key][:,2][:,None]
        uy = f[key][:,3][:,None]
        p = f[key][:,4][:,None]
        XYT = np.concatenate((XYT, np.concatenate((XY, np.full((XY.shape[0],1), time)), axis=1)), axis=0)
        UX = np.concatenate((UX, ux), axis=0)
        UY = np.concatenate((UY, uy), axis=0)
        P = np.concatenate((P, p), axis=0)
    X, y = {}, {}
    X['data'] = XYT
    y['data'] = np.concatenate((UX, UY, P), axis=1)
    return X, y




X, y = generate()
truth_xyt = X['data']
truth_data = y['data']

r_ux = np.hstack((truth_xyt, truth_data[:, 0].reshape(-1,1)))



r_uy = np.hstack((truth_xyt, truth_data[:, 1].reshape(-1,1)))
r_p = np.hstack((truth_xyt, truth_data[:, 2].reshape(-1,1)))

r_ux = FilteredData(r_ux)
r_uy = FilteredData(r_uy)
p = FilteredData(r_p)

print('r_ux shape: ', r_ux)

data = p
unique_t_values = np.unique(data[:, 2])

# PlotData(p)



def construct_graph(tri, threshold=0.44):
    graph = defaultdict(list)
    for simplex in tri.simplices:
        for i in range(3):
            u, v = sorted([simplex[i], simplex[(i+1)%3]])
            dist = distance.euclidean(tri.points[u], tri.points[v])
            if dist <= threshold:
                if v not in graph[u]:
                    graph[u].append(v)
                if u not in graph[v]:
                    graph[v].append(u)
    return graph

def find_closed_subgraphs(graph):
    visited = set()
    closed_subgraphs = []
    for vertex in graph:
        if vertex not in visited:
            subgraph = dfs(graph, vertex, set())
            boundary_edges = 0
            for u in subgraph:
                boundary_edges += len(set(graph[u]) - subgraph)
            if boundary_edges <= 2 and len(subgraph) > 2: # Ensure at least 3 nodes for a closed figure
                closed_subgraphs.append(subgraph)
            visited.update(subgraph)
    return closed_subgraphs

def get_polygons_from_closed_subgraphs(tri, closed_subgraphs):
    polygons = []
    for subgraph in closed_subgraphs:
        coords = []
        for vertex in subgraph:
            coords.append(tuple(tri.points[vertex]))
        polygons.append(Polygon(coords))
    return polygons

# ... [其他代码]

for t in unique_t_values:
    subset = data[data[:, 2] == t]
    tri = Delaunay(subset[:, :2])

    graph = construct_graph(tri)
    closed_subgraphs = find_closed_subgraphs(graph)
    
    plt.figure()
    plt.scatter(subset[:, 0], subset[:, 1], c=subset[:, 3], cmap='viridis')  # 使用p值为颜色

    polygons = get_polygons_from_closed_subgraphs(tri, closed_subgraphs)
    for polygon in polygons:
        x, y = polygon.exterior.xy
        plt.plot(x, y, 'k-')

    plt.colorbar(label='p value')
    plt.title(f"Data for t={t}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
