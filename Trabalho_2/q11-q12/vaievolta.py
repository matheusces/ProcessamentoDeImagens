from dct import pegarColuna, dct, dct2d
from idct import idct, idct2d
from PIL import Image
import numpy
import time

##PARA MOSTRAR QUE A DCT E IDCT TÁ FUNCIONANDO
ini = time.time()
im = Image.open("lena256.jpg")
height, width = im.size
im2 = Image.open("lena256.png")
im_dct = dct2d(im)
im_vai_volta = idct2d(im_dct)
im2_vai_volta = idct2d(dct2d(im2))
np_im = numpy.asarray(im_vai_volta).astype(numpy.uint8)
np_im2 = numpy.asarray(im2_vai_volta).astype(numpy.uint8)
imagem = Image.fromarray(np_im)
imagem2 = Image.fromarray(np_im2)
imagem.save("lena256_VAI_E_VOLTA.jpg")
imagem2.save("lena256_VAI_E_VOLTA.png")