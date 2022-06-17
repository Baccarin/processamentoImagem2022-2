import numpy as np
import cv2

import time

inicio = time.time()


img = cv2.imread("paisagemPropria.jpg", cv2.IMREAD_GRAYSCALE)
thresh = 127
maxValue = 255
th, dst = cv2.threshold(img, thresh, maxValue, cv2.THRESH_TRUNC)
cv2.imshow("Original", img)
cv2.imshow("THRESH_TRUNC", dst)
cv2.waitKey(0)


fim = time.time()
print(fim - inicio)
