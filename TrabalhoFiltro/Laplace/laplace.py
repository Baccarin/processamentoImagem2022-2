import numpy as np
import cv2
import time

inicio = time.time()

img = cv2.imread('paisagemPropria.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
resultado = np.vstack([img, lap])
cv2.imshow("Filtro Laplaciano", resultado)
cv2.waitKey(0)


fim = time.time()
print(fim - inicio)