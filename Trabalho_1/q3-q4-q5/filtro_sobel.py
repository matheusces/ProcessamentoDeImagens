from PIL import Image, ImageFilter
import timeit
from math import sqrt
from utils import in_file, out_file, correlacao
from filtro_media import filtro_media

# aplicando filtro sobel horizontal e vertical
def filtro_sobel(imagem):
    XSOBEL = [-1, 0, 1,
            -2, 0, 2,
            -1, 0, 1]

    YSOBEL = [-1, -2, -1,
                0, 0, 0,
                1, 2, 1]

    w, h = imagem.size
    nova_img = Image.new('RGB', (w, h))
    
    for linha in range(w):
        for coluna in range(h):
            #soma_rX = 0
            #soma_gX = 0
            #soma_bX = 0
            #soma_rY = 0
            #soma_gY = 0
            #soma_bY = 0
            # soma = 0
            # soma_1 = 0
            #i = 0
            #for m in range(linha-1, linha+2):
            #    for n in range(coluna-1, coluna+2):
            #        if m >= 0 and m < w and n >= 0 and n < h:
            #            pxl = imagem.getpixel((m,n))
                        # soma += pxl * filtroX[i]
                        # soma_1 += pxl * filtroY[i]
            #            soma_rX += pxl[0] * filtroX[i]
            #            soma_rY += pxl[0] * filtroY[i]
            #            soma_gX += pxl[1] * filtroX[i]
            #            soma_gY += pxl[1] * filtroY[i]
            #            soma_bX += pxl[2] * filtroX[i]
            #            soma_bY += pxl[2] * filtroY[i]

            #        i+=1
            soma_RGB_X = correlacao(imagem, XSOBEL, (3, 3), (linha, coluna))
            soma_RGB_Y = correlacao(imagem, YSOBEL, (3, 3), (linha, coluna))

            pxl_r = abs(soma_RGB_X[0]) + abs(soma_RGB_Y[0])
            pxl_g = abs(soma_RGB_X[1]) + abs(soma_RGB_Y[1])
            pxl_b = abs(soma_RGB_X[2]) + abs(soma_RGB_Y[2])

            nova_img.putpixel((linha, coluna), (pxl_r, pxl_g, pxl_b))
    return nova_img


if __name__ == "__main__":
    imagem_original = Image.open(in_file("Woman.jpg"))
    imagem_original = filtro_media(imagem_original, (3, 3))

    inicio = timeit.default_timer()
    imagem_filtro = filtro_sobel(imagem_original)
    fim = timeit.default_timer()

    print("Tempo de execução: {}".format(fim - inicio))
    imagem_filtro.save(out_file("WomanWithSobelFilterFinal.png"))

