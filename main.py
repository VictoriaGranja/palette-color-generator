from Kmeans import Kcluster
from palettefig import createPalette
import time
import cv2

nome = "images/colors.jpg"
img = cv2.imread(nome)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.reshape((img.shape[0] * img.shape[1], 3))

clusters = 5

dc = Kcluster(img, clusters)
print(dc)
createPalette(dc, nome)