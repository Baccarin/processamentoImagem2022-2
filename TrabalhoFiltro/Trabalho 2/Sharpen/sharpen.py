import numpy as np
import cv2
import time

inicio = time.time()

img = cv2.imread('paisagemPropria.jpg', 1)
cv2.imshow("Original",img)
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
im = cv2.filter2D(img, -1, kernel)
cv2.imshow("Sharpening",im)
cv2.waitKey(0)

fim = time.time()
print(fim - inicio)