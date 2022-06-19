import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
from scipy import ndimage
import time

def normaliza():
#NORMALIZA
    img = cv2.imread("paisagemPropria.jpg")
    img_new = cv2.normalize(img, None, alpha=0,beta=200, norm_type=cv2.NORM_MINMAX)

    img_new = img_new.astype(np.uint8) 
    cv2.imwrite('paisagemPropriaNormalizada.jpg', img_new)


    img = cv2.imread("paisagemPropriaNegative.jpg")
    img_new = cv2.normalize(img, None, alpha=0,beta=200, norm_type=cv2.NORM_MINMAX)

    img_new = img_new.astype(np.uint8) 
    cv2.imwrite('normalizandoPaisagemPropriaNegativa.jpg', img_new) 

def mediaModaMedianaGaussiana():
    #busca a imagem e trata ela
    img = cv2.imread('paisagemPropria.jpg')
    im = Image.open('paisagemPropria.jpg')
    mode = im.filter(ImageFilter.ModeFilter(size = 3))
    blur = cv2.blur(img,(3,3)) # De acordo com o valor digitado obtemos diferentes efeitos.
    median = cv2.medianBlur(img,3) # De acordo com o valor digitado obtemos diferentes resultados.
    Gaussianblur = cv2.GaussianBlur (img, (3,3), 8) # De acordo com o valor digitado obtemos diferentes resultados.

    # plota imagens lado a lado para comparação
    plt.subplot(231),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(232),plt.imshow(blur),plt.title('media')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233),plt.imshow(median),plt.title('Mediana')
    plt.xticks([]), plt.yticks([])
    plt.subplot(234),plt.imshow(mode),plt.title('Moda')
    plt.xticks([]), plt.yticks([])
    plt.subplot(235),plt.imshow(Gaussianblur),plt.title('Gaussiana')
    plt.xticks([]), plt.yticks([])
    plt.show()

    cv2.imwrite('paisagemPropriaMediana.jpg', median)


def robertSobelLaplacePrewitt():
    #declara os arrays  
    roberts_cross_v = np.array( [[1, 0 ],
                                [0,-1 ]] )
    
    roberts_cross_h = np.array( [[ 0, 1 ],
                                [ -1, 0 ]] )
    #aplica filtro
    img1 = cv2.imread("paisagemPropria.jpg",0).astype('float64')
    img1/=255.0
    vertical = ndimage.convolve( img1, roberts_cross_v )
    horizontal = ndimage.convolve( img1, roberts_cross_h )
    edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
    edged_img*=255

    img = cv2.imread("paisagemPropria.jpg")
    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    sobel = cv2.bitwise_or(sobelX, sobelY)

    lap = cv2.Laplacian(img, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))

    kernelX = np.array([[1,1,1], [0,0,0],[-1,-1,-1]])
    kernelY = np.array([[-1,0,1], [-1,0,1],[-1,0,1]])
    Prewittx = cv2.filter2D(img, -1, kernelX)
    Prewitty = cv2.filter2D(img, -1, kernelY)
    Prewitt = cv2.bitwise_or(Prewittx, Prewitty)

    # plota imagens lado a lado para comparação
    plt.subplot(231),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(232),plt.imshow(edged_img),plt.title('Roberts')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233),plt.imshow(sobel),plt.title('Sobels')
    plt.xticks([]), plt.yticks([])
    plt.subplot(234),plt.imshow(lap),plt.title('Laplacian')
    plt.xticks([]), plt.yticks([])
    plt.subplot(235),plt.imshow(Prewitt),plt.title('Prewitt')
    plt.xticks([]), plt.yticks([])
    plt.show()


def negativo():
    #aplica o filtro
    img = cv2.imread('paisagemPropria.jpg')
    img_bgr = cv2.imread('paisagemPropria.jpg')
    height, width, _ = img_bgr.shape

    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixel = img_bgr[i, j]
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
            img_bgr[i, j] = pixel
    cv2.imwrite('paisagemPropriaNegative.jpg', img_bgr)
    # plota imagens lado a lado para comparação
    plt.subplot(221),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(img_bgr),plt.title('Negative')
    plt.xticks([]), plt.yticks([])


def limiar():
    #aplica os filtros
    img = cv2.imread('paisagemPropria.jpg',0)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

    #plota as imagens
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()

def sharpen():
    # aplica o filtro
    img = cv2.imread('paisagemPropria.jpg')

    kernel = np.array([[0, -1, 0],
                    [-1, 5,-1],
                    [0, -1, 0]])
    image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

    cv2.imwrite('paisagemPropriaShapen.jpg', image_sharp)
    # plota imagens lado a lado para comparação
    plt.subplot(221),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(image_sharp),plt.title('filtro sharpen')
    plt.xticks([]), plt.yticks([])


inicio = time.time()

print("Início normaliza.")
normaliza()
fim = time.time()
print("Fim normaliza [" + str(fim - inicio) + "]")


inicio = time.time()
print("Início média, moda, mediana e gaussiana.")
#mediaModaMedianaGaussiana()
fim = time.time()
print("Fim  média, moda, mediana e gaussiana ["  + str(fim - inicio) + "]")

inicio = time.time()
print("Início robert, sobel, laplace e prewitt.")
#robertSobelLaplacePrewitt()
fim = time.time()
print("Fim robert, sobel, laplace e prewitt ["  + str(fim - inicio) + "]")


inicio = time.time()
print("Início negativo.")
#negativo()
fim = time.time()
print("Fim negativo ["  + str(fim - inicio) + "]")

inicio = time.time()
print("Início limiar.")
#limiar()
fim = time.time()
print("Fim limiar ["  + str(fim - inicio) + "]")

inicio = time.time()
print("Início sharpen.")
#sharpen()
fim = time.time()
print("Fim sharpen ["  + str(fim - inicio) + "]")
