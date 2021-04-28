import numpy as np
from PIL import Image

def simplificar(img, bits):
    img2 = img.copy()
    img2 = np.array(img2)
    passo = 2**(8 - bits)
    for line_index, linha in enumerate(img2):
        for col_index, coluna in enumerate(linha):
            for comp_index, componente in enumerate(coluna):
                resto = img2[line_index][col_index][comp_index] % passo
                if resto != 0:
                    img2[line_index][col_index][comp_index] -= resto
    return Image.fromarray(img2)


img = Image.open('lena.jpg')
img.show()

img2 = simplificar(img, 6)
img2.save('lena-6bits.jpg')

img3 = simplificar(img, 4)
img2.save('lena-4bits.jpg')