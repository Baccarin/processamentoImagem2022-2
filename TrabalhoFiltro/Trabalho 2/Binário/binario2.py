import numpy as np
import cv2
img = cv2.imread("paisagemPropria.jpg", cv2.IMREAD_GRAYSCALE)
thresh = 0
maxValue = 50 # Lembrando que o max valor é 255.
th, dst = cv2.threshold(img, thresh, maxValue, cv2.THRESH_BINARY);
cv2.imshow("Original", img)
cv2.imshow("BINARY", dst)
cv2.waitKey(0)