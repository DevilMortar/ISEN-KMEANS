import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.collections as mc
import mpl_toolkits.mplot3d.art3d as mc3d
import pylab as pl


def draw2D(samples, size=10, drawLinks=True):
    # Formatting the data:
    X, Y, links, centroids = [], [], [], set()
    for sample in samples:
        X.append(sample[0])
        Y.append(sample[1])
        if len(sample) == 4:
            links.append([sample[:2], sample[2:]])
            centroids.add((sample[2], sample[3]))
    centroids = sorted(centroids)  # before shuffling, to not depend on data order.
    random.seed(42)  # to have consistent results.
    random.shuffle(centroids)  # making less likely that close clusters have close colors.
    centroids = {cent: centroids.index(cent) for cent in centroids}
    # Colors map:
    colors = cm.rainbow(np.linspace(0, 1., len(centroids)))
    C = None  # unique color!
    if len(centroids) > 0:
        C = [colors[centroids[(sample[2], sample[3])]] for sample in samples]
    # Drawing:
    fig, ax = pl.subplots(figsize=(size, size))
    fig.suptitle('Visualisation de %d données' % len(samples), fontsize=16)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    if drawLinks:
        ax.add_collection(mc.LineCollection(links, colors=C, alpha=0.1, linewidths=1))
    ax.scatter(X, Y, c=C, alpha=0.5, s=10)
    for cent in centroids:
        ax.plot(cent[0], cent[1], c='black', marker='+', markersize=8)
    ax.autoscale()
    ax.margins(0.05)
    plt.show()

def draw3D(samples, size=10, drawLinks=True):
    # Formatting the data:
    X, Y, Z, links, centroids = [], [], [], [], set()
    for sample in samples:
        X.append(sample[0])
        Y.append(sample[1])
        Z.append(sample[2])
        if len(sample) == 6:
            links.append([sample[:3], sample[3:]])
            centroids.add((sample[3], sample[4], sample[5]))
    centroids = sorted(centroids)  # before shuffling, to not depend on data order.
    random.seed(42)  # to have consistent results.
    random.shuffle(centroids)  # making less likely that close clusters have close colors.
    centroids = {cent: centroids.index(cent) for cent in centroids}
    # Colors map:
    colors = cm.rainbow(np.linspace(0, 1., len(centroids)))
    C = None  # unique color!
    if len(centroids) > 0:
        C = [colors[centroids[(sample[3], sample[4], sample[5])]] for sample in samples]
    # Drawing:
    fig = plt.figure(figsize=(size, size))
    fig.suptitle('Visualisation de %d données' % len(samples), fontsize=16)
    ax = fig.gca(projection='3d')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_zlabel('z', fontsize=12)
    if drawLinks:
        ax.add_collection3d(mc3d.Line3DCollection(links, colors=C, alpha=0.1, linewidths=1))
    ax.scatter3D(X, Y, Z, c=C, alpha=0.5, s=10)
    for cent in centroids:
        ax.plot3D(cent[0], cent[1], cent[2], c='black', marker='+', markersize=8)
    ax.margins(0.05)
    plt.show()
