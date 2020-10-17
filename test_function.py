import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def rastrigin(x):
    A = 10
    value = A * len(x)
    for i in range(len(x)):
        value += x[i] ** 2 - A * math.cos(2 * math.pi * x[i])
    return value

if __name__ == "__main__":
    x = np.linspace(-5.12,5.12,500)
    y = np.linspace(-5.12,5.12,500)
    X,Y = np.meshgrid(x,y)
    Z = np.zeros((len(X),len(Y)))
    for i in range(len(x)):
        for j in range(len(y)):
            Z[i,j] = rastrigin([x[i],y[j]])
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X,Y,Z,cmap='rainbow')
    plt.show()