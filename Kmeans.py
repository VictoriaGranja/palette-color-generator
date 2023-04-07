from math import sqrt
import random

qtdRGB = 3

def euclidian(center, pixel):
    distance = 0
    for rgb in range(qtdRGB):
        distance += pow((center[rgb] - pixel[rgb]), 2)

    distance = int(sqrt(distance))
    return distance

 
def Kcluster(data, k):

    centers = []
    for j in range(k):
        aleatorio = random.randint(0, len(data))
        centers.append(data[aleatorio])
    
    for t in range(10):

        clusters = [[] for i in range(k)]
     
        for j in range(len(data)):
            pixel = data[j]
            bestCluster = 0
            for i in range(k):
                d = euclidian(centers[i], pixel)
                if d < euclidian(centers[bestCluster], pixel):
                    bestCluster = i

            clusters[bestCluster].append(j)

        for i in range(k):
            newCenter = [0] * qtdRGB
            if len(clusters[i]) > 0:
                for pixelIndex in clusters[i]:
                    for rgbComponent in range(qtdRGB):
                        newCenter[rgbComponent] += data[pixelIndex][rgbComponent]
                for j in range(qtdRGB):
                    newCenter[j] = int(newCenter[j]/len(clusters[i]))
                centers[i] = newCenter

    return centers
