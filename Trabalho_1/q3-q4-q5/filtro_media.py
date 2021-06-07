from PIL import Image
import random
import timeit
from utils import in_file, out_file, correlacao

# Aplicando filtro média 3x5
def filtro_media(imagem, dimensao_filtro):
    w, h = imagem.size
    nova_img = Image.new("RGB", (w, h))

    dimensao_total = dimensao_filtro[0]*dimensao_filtro[1]
    filtro = [1/dimensao_total for _ in range(dimensao_total)]

    for linha in range(w):
        for coluna in range(h):
            #soma_r = 0
            #soma_g = 0
            #soma_b = 0

            #for m in range(linha-1, linha+2):
            #    for n in range(coluna-2, coluna+3):
            #        if m >= 0 and m < w and n >= 0 and n < h:
            #            pxl = imagem.getpixel((m,n))
            #    
            #            soma_r += pxl[0]
            #            soma_g += pxl[1]
            #            soma_b += pxl[2]
            
            soma_RGB = correlacao(imagem, filtro, dimensao_filtro, (linha, coluna))

            nova_img.putpixel((linha, coluna), (int(soma_RGB[0]), int(soma_RGB[1]), int(soma_RGB[2])))
    return nova_img
            
            
            

if __name__ == "__main__":
    img = Image.open(in_file("Woman.jpg"))
    
    inicio = timeit.default_timer()
    imagem_filto = filtro_media(img, (3, 5))
    fim = timeit.default_timer()

    print("Tempo de execução: {}".format(fim - inicio))
    imagem_filto.save(out_file("WomanWithMediaFilter.png"))