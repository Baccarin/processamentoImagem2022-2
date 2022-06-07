import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage.filters import  sobel

import time
inicio = time.time()

img = imread("paisagem.jpg", as_gray=True) # carregando imagem

op_sobel = sobel(img)

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True, figsize=(12, 12))

ax = axes.ravel()

ax[0].imshow(op_sobel, cmap=plt.cm.gray)

for a in ax:
    a.axis('off')

fim = time.time()
print(fim - inicio)

plt.tight_layout()
plt.show()