import networkx as nx
import matplotlib.pyplot as plt
def plot(distance,path):
    path2edge = []
    n = len(path) - 1
    for i in range(n):
        if i < n - 1:
            path2edge.append((path[i],path[i + 1]))
        else:
            path2edge.append((path[n - 1],path[0]))
    G = nx.from_numpy_matrix(distance)
    nx.draw_networkx(G,edgelist=path2edge)
    plt.show()