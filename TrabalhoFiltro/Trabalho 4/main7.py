import numpy as np
from math import floor, ceil
from PIL import Image
from numpy import asarray
import math
import matplotlib.pyplot as plt
import time

inicio = time.time()

def save_image(img: np.ndarray, address):
    image = Image.fromarray(img)
    return image.save(address)

def get_window(full_image, location, window_size):

    window = []

    start_x = location[0] - 1
    start_y = location[1] - 1
    img_size_x, img_size_y, _ = full_image.shape
    for x in range(7):
        for y in range(7):
            try:
                if start_x + x < img_size_x and start_y + y < img_size_y:
                    pixel = full_image[start_x + x][start_y + y][0]
                    
                    window.append(pixel)
                else:
                    window.append(1)
            except IndexError:
                print("Index out of bound")
                print("___________________")
                print("location: " + str(location))
                print("image size: " + str(full_image.shape))

    return window


def lpf(image):
    row, col, _ = image.shape
    new_image = np.zeros([row, col], dtype=np.uint8)
    lpf_kernel_matrix = np.array(
        [[1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], 
        [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], 
        [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49]])

    for x in range(row):
        for y in range(col):
            window = get_window(image, [x, y], 7)
            window = np.array(window).reshape((7, 7))
            lpf_value = np.sum(np.multiply(lpf_kernel_matrix, window))
            new_image[x][y] = lpf_value
    save_image(new_image, "./img/7x7Imagem.jpg")

if __name__ == "__main__":
    image = Image.open("./img/paisagemPropria.jpg").convert('LA')
    img = asarray(image)
    print(img.shape)
    lpf(img)

    fim = time.time()
    print(fim - inicio)