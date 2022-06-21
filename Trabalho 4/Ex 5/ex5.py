import numpy as np
import cv2

matriz = np.array([[15, 18, 13, 16, 20], [30, 37, 40, 32, 28], [16, 10, 15, 18, 14], [70, 77, 66, 55, 60]])

matriz = matriz.astype(np.uint8)

lap = cv2.Laplacian(matriz, cv2.CV_64F,(3,3))
lap = np.uint8(np.absolute(lap))

print (np.matrix(lap))
# mask = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]) 

