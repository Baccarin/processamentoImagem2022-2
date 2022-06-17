from PIL import Image
from PIL import ImageFilter
import math
from random import randrange
import time

  
inicio = time.time()

# Obtendo Imagem Original
imagem_original = Image.open("paisagemPropria.jpg")
# Convertendo Imagem Original para o modo RGB
imagem = imagem_original.convert('RGB')
#imagem.show()
#print(imagem.format, imagem.size, imagem.mode)

# Obtendo tamanho das componentes x, y
# Image.width e Image.height
largura, altura = imagem.size

# Ruído gausiano {
def gausino():
    print("Processando ruído gausiano...")
    # Convertendo imagem para tons de cinza
    #cinza()
    # Modificando pixels aleatoriamente
    for x in range(largura * randrange(largura)):
        imagem.putpixel((randrange(largura), randrange(altura)), (randrange(255), randrange(255), randrange(255)))
    # Exibindo imagem modificada
    imagem.show()
#}
gausino()


# Filtro Gaussiano {
def filtro_gaussiano():
    print("Processando filtro gausiano...")
    # Percorrendo Matriz de Pixels
    for x in range(1, largura - 2):
        for y in range(1, altura - 2):
            # Obtendo componentes RGB da mascara (3x3)
            R1, G1, B1 = imagem.getpixel((x, y))
            R2, G2, B2 = imagem.getpixel((x, y + 1))
            R3, G3, B3 = imagem.getpixel((x, y - 1))
            R4, G4, B4 = imagem.getpixel((x + 1, y))
            R5, G5, B5 = imagem.getpixel((x - 1, y))
            R6, G6, B6 = imagem.getpixel((x - 1, y - 1))
            R7, G7, B7 = imagem.getpixel((x + 1, y + 1))
            R8, G8, B8 = imagem.getpixel((x + 1, y - 1))
            R9, G9, B9 = imagem.getpixel((x - 1, y + 1))
            # Aplicando os cálculos (mascara [1 2 1] [2 4 2] [1 2 1])
            R = int(((R1 * 4) + (2 * (R2 + R3 + R4 + R5)) + (1 * (R6 + R7 + R8 + R9))) / 16)
            G = int(((G1 * 4) + (2 * (G2 + G3 + G4 + G5)) + (1 * (G6 + G7 + G8 + G9))) / 16)
            B = int(((B1 * 4) + (2 * (B2 + B3 + B4 + B5)) + (1 * (B6 + B7 + B8 + B9))) / 16)
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (R, G, B))
    # Exibindo imagem modificada
    imagem.show()
#}
filtro_gaussiano()

fim = time.time()
print(fim - inicio)