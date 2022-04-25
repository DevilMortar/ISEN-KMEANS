from ast import Or
import csv
import drawLib

def loadCSV(file):
    r = []
    with open('file/' + file, newline='') as f:
        content = csv.reader(f, delimiter=',')
        for row in content:
            r.append(row)
    return r

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
    

def kMeans(data, k, maxIterations=100):
    iteration = 0
    # Initialize the centroids
    centroids = []
    for i in range(k):
        centroids.append(data[i])
    
    while True:
        # Create a list of lists
        clusters = [[] for i in range(k)]
        # Assign each point to the closest centroid
        w = -1
        for point in data:
            w+=1
            print(w)
            # Find the closest centroid
            closest = 0
            for i in range(1, k):
                if distance(point, centroids[i]) < distance(point, centroids[closest]):
                    closest = i
            # Add the point to the closest cluster
            clusters[closest].append(point)
        # Calculate the new centroids
        print("New centroids:")
        newCentroids = []
        for cluster in clusters:
            if len(cluster) == 0:
                pass
            else:
                # Calculate the middle of the cluster
                newCentroids.append((sum(cluster[i][0] for i in range(len(cluster))) / len(cluster), sum(cluster[i][1] for i in range(len(cluster)))))
        # Check if the centroids have changed
        if newCentroids == centroids or iteration == maxIterations:
            break
        # Update the centroids
        copyListIntoList(newCentroids, centroids)
        print(centroids)
        iteration += 1
        
    return centroids
                

    

    

list = cleanData(loadCSV('mock_2d_data.csv'))
#list = cleanData(loadCSV('2d_data.csv'))
#drawLib.draw2D(list, size=10, drawLinks=True)
print(kMeans(list, 3, maxIterations=100))





