import cv2 
imagen = cv2.imread('contorno.jpg')

print(cv2.__version__)
cv2.imshow('imagen',imagen)
cv2.waitKey(0) #val 0 para videso y val 1 para fotos
cv2.destroyAllWindows()
