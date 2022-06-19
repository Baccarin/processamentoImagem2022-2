import numpy as np
from PIL import Image
from numpy import asarray
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
    for x in range(3):
        for y in range(3):
            try:
                if start_x + x < img_size_x and start_y + y < img_size_y:
                    pixel = full_image[start_x + x][start_y + y][0]
                    
                    window.append(pixel)
                else:
                    window.append(1)
            except IndexError:
                print("Index out of bound")
                print("location: " + str(location))
                print("image size: " + str(full_image.shape))

    return window


def lpf(image):
    row, col, _ = image.shape
    new_image = np.zeros([row, col], dtype=np.uint8)
    lpf_kernel_matrix = np.array(
        [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])

    for x in range(row):
        for y in range(col):
            window = get_window(image, [x, y], 3)
            window = np.array(window).reshape((3, 3))
            lpf_value = np.sum(np.multiply(lpf_kernel_matrix, window))
            new_image[x][y] = lpf_value
    save_image(new_image, "./img/3x3Imagem.jpg")

if __name__ == "__main__":
    image = Image.open("./img/paisagemPropria.jpg").convert('LA')
    img = asarray(image)
    print(img.shape)
    lpf(img)

    fim = time.time()
    print(fim - inicio)