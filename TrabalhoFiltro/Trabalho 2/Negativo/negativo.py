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

# Negativo {
def negativo():
    print("Processando negativo...")
    # Convertendo em escala de cinza
    #cinza()
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            # Obtendo componente RGB pixel atual
            R, G, B = imagem.getpixel((x, y))
            # Modificando componentes RGB do pixel atual
            imagem.putpixel((x, y), (255 - R, 255 - G, 255 - B))
    # Exibindo imagem modificada
    imagem.show()   
#}
negativo()


fim = time.time()
print(fim - inicio)