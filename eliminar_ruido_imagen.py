from cv2 import cv2
import numpy as  np

original  = cv2.imread('monedas.jpg')
grises = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
#esta linea elimina el ruido haciendo un blur
blur = cv2.GaussianBlur(grises,(3,3),0)
#mas eliminaciond de ruido
canny  = cv2.Canny(blur,60,100)



#show results 
cv2.imshow('grises',grises)
cv2.imshow('Blur gauss',blur)
cv2.imshow('canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()