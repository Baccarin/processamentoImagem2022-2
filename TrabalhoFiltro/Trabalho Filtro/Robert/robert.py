from PIL import Image
from PIL import ImageFilter
import math
from random import randrange

# Obtendo Imagem Original
imagem_original = Image.open("paisagemPropria.jpg")
# Convertendo Imagem Original para o modo RGB
imagem = imagem_original.convert('RGB')
#imagem.show()
#print(imagem.format, imagem.size, imagem.mode)

# Obtendo tamanho das componentes x, y
# Image.width e Image.height
largura, altura = imagem.size

# Escala de Cinza {
def cinza():
    print("Processando escala de cinza...")
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            # Obtendo componente RGB do pixel atual
            R, G, B = imagem.getpixel((x, y))
            # Aplicando o padrão de vídeo digital ITU-R 601-2
            L = int((R * 299/1000) + (G * 587/1000) + (B * 114/1000))
            imagem.putpixel((x, y), (L, L, L))
    # Exibindo imagem modificada
    imagem.show()
#}
#cinza()

# roberts {
def roberts():
    print("Processando operador de roberts...")
    #Convertendo imagem para tons de cinza
    cinza()
    # Percorrendo Matriz de Pixels
    for x in range(1, largura - 2):
        for y in range(1, largura - 2):
            # Obtendo componentes RGB da mascara (3x3)
            R0, G0, B0 = imagem.getpixel((x - 1, y - 1))
            R1, G1, B1 = imagem.getpixel((x, y - 1))
            R2, G2, B2 = imagem.getpixel((x + 1, y - 1))
            R3, G3, B3 = imagem.getpixel((x - 1, y))
            R4, G4, B4 = imagem.getpixel((x, y))
            R5, G5, B5 = imagem.getpixel((x + 1, y))
            R6, G6, B6 = imagem.getpixel((x - 1, y + 1))
            R7, G7, B7 = imagem.getpixel((x, y + 1))
            R8, G8, B8 = imagem.getpixel((x + 1, y + 1))
            # Convolução (mascara horizontal)
            eixo_x = (-1 * R2) + (1 * R4)
            #eixo_x = eixo_x / 4
            # Convolução (mascara vertica)
            eixo_y = (-1 * R0)
            #eixo_y = eixo_x / 4
            # Obtendo valor de gradiente
            gradiente = math.sqrt((eixo_x ** 2) + (eixo_y ** 2))
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (int(gradiente), int(gradiente), int(gradiente)))
    # Exibindo imagem modificada
    imagem.show()
#}
roberts()