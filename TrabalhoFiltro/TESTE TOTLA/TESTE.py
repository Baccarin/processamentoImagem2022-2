#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# Binarização {
def binarizacao(limiar):
    print("Processando binarização...")
    # Convertendo em escala de cinza
    #cinza()
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


# histograma() {
def histograma():
    print("Processando histograma...")
    # Convertendo em escala de cinza
    cinza()
    intensidade = []
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            R, G, B = imagem.getpixel((x, y))
            intensidade.append(R);

    Xmin = min(intensidade)
    Xmax = max(intensidade)
    print({x:intensidade.count(x) for x in set(intensidade)})
    return Xmin, Xmax
#}
#histograma()


# realce() {
def realce():
    print("Processando realce...")
    # Obtendo Xmin e Xmax baseado no histograma
    Xmin, Xmax = histograma()
    # Aplicando os cálculos
    a = 255 / (Xmax - Xmin)
    b = -a * Xmin
    # Percorrendo Matriz de Pixels
    for x in range(largura):
        for y in range(altura):
            # Obtendo componentes RGB do pixel atual
            R, G, B = imagem.getpixel((x, y))
            # Aplicando os cálculos para obter nova componente
            Y = int(a * R + b)
            # Modificando componentes do pixel atual
            imagem.putpixel((x, y), (Y, Y, Y))
    # Exibindo imagem modificada
    imagem.show()
#}
#realce()

