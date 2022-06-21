import numpy as np
import cv2

img = cv2.imread('img.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(img, cv2.CV_64F)

img_new = np.vstack([lap])

cv2.imwrite('laplace.jpg', img_new) 
