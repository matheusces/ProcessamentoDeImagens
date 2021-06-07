from dct import pegarColuna, dct, dct2d
from idct import idct, idct2d
from PIL import Image
import numpy
import time


def mostImportant(npmatrix, n, height, width):
    aux = npmatrix.flatten()
    aux[0] = 0
    most_imp_index_flatten = numpy.argpartition(numpy.absolute(aux), -n)[-n:]
    most_imp_index_2d = []
    for i in most_imp_index_flatten:
        most_imp_index_2d.append(tuple([i//width, i % width]))
    result = numpy.zeros((height, width))
    result[0][0] = npmatrix[0][0]
    for j in most_imp_index_2d:
        result[j[0]][j[1]] = npmatrix[j[0]][j[1]]
    return result

ini = time.time()
im = Image.open("lena256.jpg")
height, width = im.size
im_dct = dct2d(im)

##EXEMPLOS DOS N NÍVEIS MAIS IMPORTANTES

#8 NÍVEIS MAIS IMPORTANTES

np_8 = mostImportant(numpy.asarray(im_dct), 8, height, width)
np_80 = idct2d(np_8.tolist())
np_80 = numpy.asarray(np_80).astype(numpy.uint8)
imagem_8 = Image.fromarray(np_80)
imagem_8.save("lena256_8.jpg")

#16 NÍVEIS MAIS IMPORTANTES

np_8 = mostImportant(numpy.asarray(im_dct), 16, height, width)
np_80 = idct2d(np_8.tolist())
np_80 = numpy.asarray(np_80).astype(numpy.uint8)
imagem_16 = Image.fromarray(np_80)
imagem_16.save("lena256_16.jpg")

#32 NÍVEIS MAIS IMPORTANTES

np_8 = mostImportant(numpy.asarray(im_dct), 32, height, width)
np_80 = idct2d(np_8.tolist())
np_80 = numpy.asarray(np_80).astype(numpy.uint8)
imagem_32 = Image.fromarray(np_80)
imagem_32.save("lena256_32.jpg")

#1024 NÍVEIS MAIS IMPORTANTES

np_16 = mostImportant(numpy.asarray(im_dct), 1024, height, width)
np_160 = numpy.asarray(idct2d(np_16.tolist())).astype(numpy.uint8)
imagem_1024 = Image.fromarray(np_160)
#imagem_1024.show
imagem_1024.save("lena256_1024.jpg")

fim = time.time()



print(f"O CÓDIGO DEMOROU {fim-ini:.2f} SEGUNDOS")

