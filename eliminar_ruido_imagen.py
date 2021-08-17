from cv2 import cv2
import numpy as  np

valkernel = 11
valgauss = 3
original  = cv2.imread('monedas2.jpg')
grises = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
#esta linea elimina el ruido haciendo un blur
blur = cv2.GaussianBlur(grises,(valgauss,valgauss),0)
#mas eliminaciond de ruido
canny  = cv2.Canny(blur,60,100)

kernel = np.ones((valkernel,valkernel),np.uint8)
cierre_contornos  =cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel) 

contornos,jerarquia = cv2.findContours(cierre_contornos.copy(),
cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print('Monedad encontradas:{}'.format(len(contornos)))

#dibujando contornos en imagen original
cv2.drawContours(original,contornos,-1,(100,0,150),4)

#show results 
cv2.imshow('grises',grises)
cv2.imshow('Blur gauss',blur)
cv2.imshow('canny',canny)
cv2.imshow('cierre de contornos',cierre_contornos)
cv2.imshow('original',original)
cv2.waitKey(0)
cv2.destroyAllWindows()