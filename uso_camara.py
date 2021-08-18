import cv2 as cv

captura_video = cv.VideoCapture(0)
if not(captura_video.isOpened()):
    print('no hay camara')
    exit()

while True:
   tipo_de_cam,camara = captura_video.read()
   grises = cv.cvtColor(camara,cv.COLOR_BGR2GRAY)
   cv.imshow('en vivo',grises)
   if(cv.waitKey(1) == ord('q')):#detener programa
        break
    
captura_video.release()
cv.destroyAllWindows()