from PIL import Image, ImageFilter
import timeit
from math import sqrt
from utils import in_file, out_file

# aplicando filtro de sobel
def filtrar(imagem, filtro):
    w, h = imagem.size
    # nova_img = Image.new("RGB", (w, h))
    nova_img = Image.new('L', (w, h))

    for linha in range(w):
        for coluna in range(h):
            # soma_r = 0
            # soma_g = 0
            # soma_b = 0

            lum = 0
            i = 0
            for m in range(linha-1, linha+2):
                for n in range(coluna-1, coluna+2):
                    if m >= 0 and m < w and n >= 0 and n < h:
                        pxl = imagem.getpixel((m,n))
                        lum += pxl * filtro[i]
                        # soma_r += pxl[0]*filtro[i]
                        # soma_g += pxl[1]*filtro[i]
                        # soma_b += pxl[2]*filtro[i]
                    i+=1

            nova_img.putpixel((linha, coluna), lum)
    return nova_img

# aplicando filtro sobel horizontal e vertical
def filtro_sobel(imagem):
    XSOBEL = ImageFilter.Kernel((3,3), 
    [
        -1, 0, 1,
        -2, 0, 2,
        -1, 0, 1
    ], 1, 0)

    YSOBEL = ImageFilter.Kernel((3,3), 
    [
        -1, -2, -1,
        0, 0, 0,
        1, 2, 1
    ], 1, 0)


    # XSOBEL = [-1, 0, 1,
    #         -2, 0, 2,
    #         -1, 0, 1]

    # YSOBEL = [-1, -2, 1,
    #         0, 0, 0,
    #         1, 2, 1]

    hsobel = imagem.filter(XSOBEL)
    vsobel = imagem.filter(YSOBEL)
    # hsobel = filtrar(imagem, XSOBEL)
    # vsobel = filtrar(imagem, YSOBEL)

    w, h = imagem.size
    # imagem_filtrada = Image.new('RGB', (w, h))
    imagem_filtrada = Image.new('L', (w, h))


    for i in range(w):
        for j in range(h):
            pxl_hsobel = hsobel.getpixel((i, j))
            pxl_vsobel = vsobel.getpixel((i, j))
            
            # pxl_filtrado = []
            # for k in range(3):
            #     if(pxl_hsobel[k] < 0):
            #         pxl_hsobel[k] = pxl_hsobel[k] * -1

            #     if(pxl_vsobel[k] < 0):
            #         pxl_vsobel[k] = pxl_vsobel[k] * -1

            #     pxl_filtrado.append(min(pxl_hsobel[k]+pxl_vsobel[k], 255))
            if(pxl_hsobel < 0):
                pxl_hsobel = pxl_hsobel * -1

            if(pxl_vsobel < 0):
                pxl_vsobel = pxl_vsobel * -1

            valor = sqrt(pxl_vsobel**2 + pxl_hsobel**2)
            valor = int(min(valor, 255))
            imagem_filtrada.putpixel((i, j), valor)
    
    return imagem_filtrada

if __name__ == "__main__":
    # converter para escala de cinza
    image_original = Image.open(in_file("Woman.jpg")).convert('L')

    inicio = timeit.default_timer()
    imagem_filto = filtro_sobel(image_original)
    fim = timeit.default_timer()

    print("Tempo de execução: {}".format(fim - inicio))
    imagem_filto.save(out_file("WomanWithSoberFilter.png"))
