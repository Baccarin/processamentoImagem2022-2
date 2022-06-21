import numpy as np 
import cv2

matriz = np.array([[15, 18, 13, 16, 20], 
                   [30, 37, 40, 32, 28], 
                   [16, 10, 15, 18, 14], 
                   [70, 77, 66, 55, 60]])

media = cv2.blur(matriz, (5,5))

print (np.matrix(media))