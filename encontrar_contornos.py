from cv2 import cv2

#funcion find countors requeiere:
# imgen umbral , modo y metodo(simple o none)
imagen = cv2.imread('contorno.jpg')
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

#el guin bajo es para almacenar un valor de retorno que vale v
_,umbral = cv2.threshold(grises,50,255,cv2.THRESH_BINARY)
contorno,jerarquia = cv2.findContours(umbral
    ,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
                    
#es -1 para que encuentre todos los contornos
cv2.drawContours(imagen,contorno,-1,(184,80,56),3)


#show 
cv2.imshow('Imagen en grises',grises)
cv2.imshow('Imagen original',imagen)
cv2.imshow('Imagen umbral',umbral)

cv2.waitKey(0) #val 0 para videso y val 1 para fotos
cv2.destroyAllWindows() 