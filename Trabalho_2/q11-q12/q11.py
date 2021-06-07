from dct import pegarColuna, dct, dct2d
from idct import idct, idct2d
from PIL import Image, ImageFile
import numpy
import time


ini = time.time()
im = Image.open("lena256.jpg")
width, height = im.size
dctim = dct2d(im)
fim = time.time()
save = dctim[0][0]
print(f"O CÓDIGO DEMOROU {fim-ini:.2f} SEGUNDOS")
print(f"VALOR DO NÍVEL DC É {save}")
dctim[0][0] = 0.0
np_dctim = numpy.array(dctim)
np_dctim = numpy.absolute(dctim)
im11 = Image.fromarray((np_dctim*(255.0/numpy.max(np_dctim))))
im11 = im11.convert("L")
im11.save("lena256_DCT.jpg")
