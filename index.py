import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.collections as mc
import pylab as pl
import csv


def loadCSV(file):
    r = []
    with open('file/' + file, newline='') as f:
        content = csv.reader(f, delimiter=',')
        for row in content:
            r.append(row)
    return r


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
