import numpy as np
import cv2


img = cv2.imread("img.png", cv2.IMREAD_GRAYSCALE)
m, n = img.shape

mask = np.copy(img)

img_new = np.zeros([m,n])

for i in range(1, m-1):
    for j in range(1, n-1):
        gx = (img[i - 1][j - 1] + 2*img[i][j - 1] + img[i + 1][j - 1]) - (img[i - 1][j + 1] + 2*img[i][j + 1] + img[i + 1][j + 1])
        gy = (img[i - 1][j - 1] + 2*img[i - 1][j] + img[i - 1][j + 1]) - (img[i + 1][j - 1] + 2*img[i + 1][j] + img[i + 1][j + 1])
        img_new[i][j] = min(255, np.sqrt(gx**2 + gy**2))
  

img_new = img_new.astype(np.uint8) 
cv2.imwrite('sobel.jpg', img_new) 