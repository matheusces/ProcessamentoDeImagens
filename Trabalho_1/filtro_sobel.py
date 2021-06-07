from PIL import Image, ImageFilter
import timeit
from math import sqrt
from utils import in_file, out_file
from filtro_media import filtro_media

# aplicando filtro sobel horizontal e vertical
def filtro_sobel(imagem, filtroX, filtroY):
    w, h = imagem.size
    nova_img = Image.new('RGB', (w, h))

    for linha in range(w):
        for coluna in range(h):
            soma_rX = 0
            soma_gX = 0
            soma_bX = 0
            soma_rY = 0
            soma_gY = 0
            soma_bY = 0
            # soma = 0
            # soma_1 = 0
            i = 0
            for m in range(linha-1, linha+2):
                for n in range(coluna-1, coluna+2):
                    if m >= 0 and m < w and n >= 0 and n < h:
                        pxl = imagem.getpixel((m,n))
                        # soma += pxl * filtroX[i]
                        # soma_1 += pxl * filtroY[i]
                        soma_rX += pxl[0] * filtroX[i]
                        soma_rY += pxl[0] * filtroY[i]
                        soma_gX += pxl[1] * filtroX[i]
                        soma_gY += pxl[1] * filtroY[i]
                        soma_bX += pxl[2] * filtroX[i]
                        soma_bY += pxl[2] * filtroY[i]

                    i+=1

            pxl_r = abs(soma_rX) + abs(soma_rY)
            pxl_g = abs(soma_gX) + abs(soma_gY)
            pxl_b = abs(soma_bX) + abs(soma_bY)

            nova_img.putpixel((linha, coluna), (pxl_r, pxl_g, pxl_b))
    return nova_img


if __name__ == "__main__":
    XSOBEL = [-1, 0, 1,
            -2, 0, 2,
            -1, 0, 1]

    YSOBEL = [-1, -2, -1,
                0, 0, 0,
                1, 2, 1]\

    imagem_original = Image.open(in_file("Woman.jpg"))
    imagem_original = filtro_media(imagem_original)

    inicio = timeit.default_timer()
    imagem_filtro = filtro_sobel(imagem_original, XSOBEL, YSOBEL)
    fim = timeit.default_timer()

    print("Tempo de execução: {}".format(fim - inicio))
    imagem_filtro.save(out_file("WomanWithSobelFilterFinal.png"))

