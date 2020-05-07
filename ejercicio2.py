import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('contr2.jpg')

#realizmos el histograma de la imagen original 
histOriginal = cv2.calcHist([imagen], [0], None, [256], [0, 256])

img = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)
Outlier = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)


for i in range(10):
    for j in range(10):
        Outlier[i][j] = 0

cv2.imshow('Outlier',Outlier)
cv2.imwrite('Out.jpg',Outlier)
histimg = cv2.calcHist([img], [0], None, [256], [0, 256])
histOut = cv2.calcHist([Outlier], [0], None, [256], [0, 256])
 

plt.plot(histOut, color='red' )
plt.plot(histOriginal, color = 'black')
plt.xlabel('Intensidad de iluminacion')
plt.ylabel('Cantidad de pixeles')
plt.show()
