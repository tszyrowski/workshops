'''
author: T

from: https://en.wikipedia.org/wiki/Matplotlib
'''
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm               # for 3D plot
from mpl_toolkits.mplot3d import Axes3D # for 3D plot

# LINE PLOT
def linePlot():
    a = np.linspace(0,10,100)
    b = np.exp(-a)
    plt.plot(a,b)

# HISTOGRAM
def histogram():
    fig = plt.figure()
    x = np.random.normal(size=200)
    plt.hist(x,bins=30)

# SCATTER
def scatter():
    fig = plt.figure()
    xVal = np.random.rand(100)
    yVal = np.random.rand(100)
    plt.scatter(xVal, yVal)

def plot3D():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)

linePlot()
histogram()
scatter()
plot3D()

plt.show()