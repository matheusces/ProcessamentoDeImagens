from scipy import signal, misc, fft, ndimage
from skimage import io, feature
import matplotlib.pyplot as plt
from matplotlib import image
import matplotlib.patches as patches
from PIL import Image, ImageFilter
import numpy as np


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
            if m >= 0 and m < w and n >= 0 and n < h and i<dimensao_filtro[0] and j<dimensao_filtro[1]:
                pxl = imagem.getpixel((m,n))
                pxl_filtro = filtro.getpixel((i, j))

                soma += pxl * pxl_filtro
            j+=1
        i+=1

    return soma

face = Image.open('./input/Woman.jpg').convert('L')
eye =  Image.open('./input/Woman_eye.jpg').convert('L')
# print(eye.dtype)
# print(eye.shape)
# print(type(eye_arr))
# print(type(eye_img))

#face = face - face.mean()
# eye = eye - eye.mean()
# face = face - face_mean
# eye = eye - eye_mean
eye_height = eye.height
eye_width = eye.width
#face = face + np.random.randn(*face.shape) * 50  # add noise
#corr = correlacao(face, FILTRO_MEDIA, (3,5), coordinator)
w, h = face.size
nova_img = Image.new("RGB", (w, h))

for linha in range(w):
    for coluna in range(h):
        soma_RGB = correlacaoYIQ(face, eye, (eye_width, eye_height), (linha,coluna))
        nova_img.putpixel((linha, coluna), soma_RGB)
print(type(nova_img))

new_img_arr = np.asarray(nova_img)

y, x = np.unravel_index(np.argmax(new_img_arr), new_img_arr.shape)  # find the match

fig, (ax_orig, ax_eye, ax_corr) = plt.subplots(1, 3, figsize=(15, 6))
rect = patches.Rectangle((x,y),eye_width,eye_height, edgecolor='r', facecolor="none")
ax_orig.imshow(face, cmap='gray')
ax_orig.set_title('Original')
ax_orig.set_axis_off()
ax_eye.imshow(eye, cmap='gray')
ax_eye.set_title('Eye')
ax_eye.set_axis_off()
ax_corr.imshow(sobel, cmap='gray')
ax_corr.set_title('Cross-correlation')
ax_corr.set_axis_off()
ax_orig.add_patch(rect)
fig.savefig('./output/2d_correlation_output.png')