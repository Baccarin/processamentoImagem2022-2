import numpy as np 
import cv2

img = cv2.imread('img.png', 0)

m, n = img.shape

img_new = np.zeros([m,n])

for i in range (1, m-1):
    for j in range (1, n-1):
        temp = [img [i-1, j-1],
                img [i-1, j],
                img [i-1, j+1],
                img [i, j-1],
                img [i, j],
                img [i, j+1],
                img [i+1, j-1],
                img [i+1, j],
                img [i+1, j+1]
                ]
        temp = sorted(temp)
        img_new[i,j] = temp[4]

img_new = img_new.astype(np.uint8)
cv2.imwrite('filtroMediana.png', img_new)