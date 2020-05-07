
import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('contr2.jpg')

#realizmos el histograma de la imagen original 
histOriginal = cv2.calcHist([imagen], [0], None, [256], [0, 256])




imagen_original = cv2.imread('contr2.jpg')
imagen_resultado = cv2.imread('contr2.jpg')

##################GENERACION DE OUTLIER##################################

img = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)
Outlier = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)
res = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)


for i in range(10):
    for j in range(10):
        Outlier[i][j] = 0

cv2.imshow('Outlier',Outlier)
cv2.imwrite('Out.jpg',Outlier)
histimg = cv2.calcHist([img], [0], None, [256], [0, 256])
histOut = cv2.calcHist([Outlier], [0], None, [256], [0, 256])
#####################################################################



plt.plot(histOut, color='red' )
plt.plot(histOriginal, color = 'black')
plt.xlabel('Intensidad de iluminacion')
plt.ylabel('Cantidad de pixeles')
#plt.show()

# Convertir las imágenes del formato BGR a RGB porque matplotlib acepta 
# imagenes en formato RGB 
imagen_original = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
imagen_resultado = cv2.cvtColor(imagen_resultado, cv2.COLOR_BGR2RGB)


####################OUTLIER###############################################

#Detallamos los valores de las variables de Contrast stretching 
a = 0   # límite inferior
b = 255 # límite superior
#c = 69
#d = 149
c = np.min(imagen_original)  # El menor valor de los pixeles
d = np.max(imagen_original)  # El mayor valor de los pixeles

#porcentaje=5

#Funcion para crear limites en nuestro rango del histograma 
#para asi  afrontar el outliyer
def limite(porcentaje):#Mandamos el porcentaje que queremos reducir
        longi=d-c   #calculamos la longitud del rango
        limite=(longi*porcentaje)/100 #calculamos el limite a partir del porcentaje
        return (int(limite))

newc=c-limite(5)# El menor valor  en un limite de 5% 
newd=d+limite(5)# El menor valor en un limite de 95%



print("estos son")

#print(newc,newd)
alto, ancho, canales = imagen_original.shape 
#c,d= limite(histOut,alto*ancho,5)
print(c,d)
print(min,max)


def point_operatorOutlier(pixel_RGB):#Utilizamos operador punto
    return (pixel_RGB - newc) * ((b - a) / (newd - newc) + a)#Remplazamos los nuevos valores de c y d ya reducidos

for x in range(alto):
    for y in range(ancho):
        re = point_operatorOutlier(Outlier[x][y])#aplicamos el operador punto 
        if(re<0):
            res[x][y]=0  
        elif(re>255):
            res[x][y]=255
        else:
            res[x][y]=re
       
hisRes = cv2.calcHist([res], [0], None, [256], [0, 256])
#cv2.imshow('Resultado',res)        
cv2.imwrite('res.jpg',res)#Guardamos la imagen resultante        


plt.plot(histOut, color='red' )
plt.plot(histOriginal, color = 'black')
plt.plot(hisRes, color='green')
plt.xlabel('Intensidad de iluminacion')
plt.ylabel('Cantidad de pixeles')
plt.show()




