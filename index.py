from ast import Or
import csv
from email import header
import drawLib

def loadCSV(file):
    r = []
    with open('file/' + file, newline='') as f:
        content = csv.reader(f, delimiter=',')
        for row in content:
            r.append(row)
    return r

def saveCSV(file, data):
    with open('file/' + file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        header = ['x', 'y', 'centroid_x', 'centroid_y']
        writer.writerow(header)
        for row in data:
            writer.writerow(row)

def cleanData(data):
    # Remove the first line
    data.pop(0)
    # Create a list of tuples
    data = [tuple(map(float, row)) for row in data]
    return data

def distance(Point1, Point2):
    return ((Point1[0] - Point2[0]) ** 2 + (Point1[1] - Point2[1]) ** 2) ** 0.5

def copyListIntoList(origin, destination):
    for i in range(len(origin)):
        destination[i] = origin[i]
    
def assignCluster(data, centroids):
    clusters = [[] for i in range(len(centroids))]
    for point in data:
        closest = 0
        for i in range(1, len(centroids)):
            if distance(point, centroids[i]) < distance(point, centroids[closest]):
                closest = i
        clusters[closest].append(point)
    return clusters

def updateCentroids(clusters):
    centroids = []
    for cluster in clusters:
        if len(cluster) == 0:
            pass
        else:
            # Calculate the middle of the cluster
            centroids.append((sum(cluster[i][0] for i in range(len(cluster))) / len(cluster), sum(cluster[i][1] for i in range(len(cluster)))/ len(cluster)))
    return centroids


def kMeans(data, k, maxIterations=100):
    iteration = 0
    # Initialize the centroids
    centroids = []
    for i in range(k):
        centroids.append(data[i])
    while True:
        # Assign the clusters
        clusters = assignCluster(data, centroids)
        # Calculate the new centroids
        newCentroids = updateCentroids(clusters)
        # Check if the centroids have changed or if the maximum number of iterations has been reached
        if newCentroids == centroids or iteration == maxIterations:
            break
        # Update the centroids
        copyListIntoList(newCentroids, centroids)
        iteration += 1
    # create exporting list
    list = []
    for i in range(len(clusters)):
        for point in clusters[i]:
            newPoint = []
            newPoint.append(point[0])
            newPoint.append(point[1])
            newPoint.append(centroids[i][0])
            newPoint.append(centroids[i][1])
            list.append(newPoint)
    return list

      
                

    

    

data = cleanData(loadCSV('2d_data.csv'))
#list = cleanData(loadCSV('2d_data.csv'))
#drawLib.draw2D(list, size=10, drawLinks=True)
list = kMeans(data, 20, maxIterations=200)
drawLib.draw2D(list, size=10, drawLinks=True)
saveCSV('export.csv', list)






