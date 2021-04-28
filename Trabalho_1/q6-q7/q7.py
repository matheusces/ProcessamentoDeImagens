from scipy import signal, misc, fft
import scipy
import matplotlib.pyplot as plt
from matplotlib import image
import matplotlib.patches as patches
from PIL import Image, ImageFilter
import numpy as np
import cv2 as cv

def correlacaoYIQ(imagem, filtro, dimensao_filtro, tupla_pixel):
    w, h = imagem.size

    linha = tupla_pixel[0]
    coluna = tupla_pixel[1]
    var_linha = int(dimensao_filtro[0]/2) # variante da linha do inicio ao fim
    var_coluna = int(dimensao_filtro[1]/2) # variante da coluna do inicio ao fim
    
    soma = 0
    i = j = 0
    for m in range(linha-var_linha, linha+var_linha+1):
        j = 0
        for n in range(coluna-var_coluna, coluna+var_coluna+1):
            if m >= 0 and m < w and n >= 0 and n < h:
                pxl = imagem.getpixel((m,n))

                x = np.array(pxl)
                y = np.array(filtro.getpixel((i, j)))

                soma += x.dot(y)
            j+=1
        i+=1
    
    return soma

face = Image.open('Woman.jpg')
eye =  Image.open('Woman_eye.jpg')
# print(eye.dtype)
# print(eye.shape)
# print(type(eye_arr))
# print(type(eye_img))

#face = face - face.mean()
# eye = eye - eye.mean()
# face = face - face_mean
# eye = eye - eye_mean
coordinator = face.getpixel((1,1))
print(coordinator)
eye_height = eye.height
eye_width = eye.width
#face = face + np.random.randn(*face.shape) * 50  # add noise
#corr = correlacao(face, FILTRO_MEDIA, (3,5), coordinator)
corr = correlacaoYIQ(face, eye, (eye_width, eye_height), (1,1))
#y, x = np.unravel_index(np.argmax(corr), np.asarray(corr).shape)  # find the match
#corr.save('corr.png')
# fig, (ax_orig, ax_eye, ax_corr) = plt.subplots(1, 3, figsize=(15, 6))
# rect = patches.Rectangle((x-eye_width/2,y-eye_height/2),eye_width,eye_height, edgecolor='r', facecolor="none")
# ax_orig.imshow(face, cmap='gray')
# ax_orig.set_title('Original')
# ax_orig.set_axis_off()
# ax_eye.imshow(eye, cmap='gray')
# ax_eye.set_title('Eye')
# ax_eye.set_axis_off()
# ax_corr.imshow(sobel, cmap='gray')
# ax_corr.set_title('Cross-correlation')
# ax_corr.set_axis_off()
# ax_orig.add_patch(rect)
# fig.savefig('out2.png')
