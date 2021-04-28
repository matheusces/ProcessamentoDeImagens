import numpy as np
from PIL import Image


def rgb_to_yiq(img):
    img2 = img.copy()
    np_img = np.array(img2).astype(np.float64)
    YIQ = np.array([[0.299, 0.587, 0.114],
                    [0.596, -0.274, -0.322],
                    [0.211, -0.523, 0.312]])
    for line_index, linha in enumerate(np_img):
        for col_index, coluna in enumerate(linha):
            np_img[line_index][col_index] = np.dot(YIQ, np.array(coluna).T).T
    return np_img


def yiq_to_rgb(img):
    np_img = np.copy(img)
    np_img = np_img.astype(np.float64)
    RGB = np.array([[1, 0.956, 0.621],
                    [1,-0.272, -0.647],
                    [1,-1.106, 1.703]])

    for line_index, linha in enumerate(np_img):
        for col_index, coluna in enumerate(linha):
            novo_trio = np.dot(RGB, coluna.T).T
            novo_trio = np.around(novo_trio).astype(np.uint8)
            novo_trio = np.clip(novo_trio, 0, 255)
            np_img[line_index][col_index] = novo_trio
    np_img = np_img.astype(np.uint8)
    return Image.fromarray(np_img)


#EXECUTANDO


img = Image.open('Monty-Python.jpg')
img.show()

#EXIBINDO A CONVERSÃO PARA YIQ
np_img2 = np.around(rgb_to_yiq(img)).astype(np.uint8)
np_img2 = np.clip(np_img2, 0, 255)
img2 = Image.fromarray(np_img2)
img2.save('Monty-Python-YIQ.jpg')

#EXIBINDO A CONVERSÃO RGB-YIQ-RGB
img3 = yiq_to_rgb(rgb_to_yiq(img))
img3.save('Monty-Python-YIQ-RGB.jpg')