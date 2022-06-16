from PIL import Image
from PIL import ImageFilter
import math
from random import randrange

# Obtendo Imagem Original
imagem_original = Image.open("paisagemPropria.jpg")
# Convertendo Imagem Original para o modo RGB
imagem = imagem_original.convert('RGB')
imagem.show()
#print(imagem.format, imagem.size, imagem.mode)

# Obtendo tamanho das componentes x, y
# Image.width e Image.height
largura, altura = imagem.size


# Binarização {
def binarizacao(limiar):
    print("Processando binarização...")
    # Convertendo em escala de cinza
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            # Obtendo componentes RGB pixel atual
            R, G, B = imagem.getpixel((x, y))
            # Modificando componentes RGB do pixel atual
            if ((R + G + B) / 3 <= limiar):
                imagem.putpixel((x, y), (0, 0, 0))
            else:
                imagem.putpixel((x, y), (255, 255, 255))
    # Exibindo imagem modificada
    imagem.show()
#}
binarizacao(120)
