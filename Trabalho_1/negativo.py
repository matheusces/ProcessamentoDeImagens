import numpy as np
from PIL import Image
from conversao import rgb_to_yiq, yiq_to_rgb

def negativo(img, Red=False, Green=False, Blue=False):
    img2 = np.array(img)
    for line_index, linha in enumerate(img2):
        for col_index, coluna in enumerate(linha):
            for comp_index, componente in enumerate(coluna):
                if (Red and comp_index == 0):
                    img2[line_index][col_index][0] = 255-componente
                if (Green and comp_index == 1):
                    img2[line_index][col_index][1] = 255-componente
                if (Blue and comp_index == 2):
                    img2[line_index][col_index][2] = 255-componente
    return Image.fromarray(img2)

def negativoY(img):
    np_img = rgb_to_yiq(img)
    for line_index, linha in enumerate(np_img):
        for col_index, coluna in enumerate(linha):
            np_img[line_index][col_index][0] = 255.0 - (np_img[line_index][col_index][0])
            break
    return yiq_to_rgb(np_img)


img = Image.open('Monty-Python.jpg')

#NEGATIVO EM R,G,B
img2 = negativo(img, Red=True, Green=True, Blue=True)
img2.save("Monty-Python-neg-RGB.jpg")

#NEGATIVO EM Y
img2 = negativoY(img)
img2.save("Monty-Python-neg-Y.jpg")