from PIL import Image
import timeit
from utils import in_file, out_file

# Aplicando filtro mediana 3x5
def filtro_mediana(imagem):
    w, h = imagem.size
    nova_img = Image.new("RGB", (w, h))

    for linha in range(w):
        for coluna in range(h):
            lista_r = []
            lista_g = []
            lista_b = []

            for m in range(linha-1, linha+2):
                for n in range(coluna-2, coluna+3):
                    if m >= 0 and m < w and n >= 0 and n < h:
                        pxl = imagem.getpixel((m,n))
                        
                        lista_r.append(pxl[0]) 
                        lista_g.append(pxl[1]) 
                        lista_b.append(pxl[2])
                    else:
                        # Adicionando 0 para que o número de elementos de cada lista seja 15
                        lista_r.append(0) 
                        lista_g.append(0) 
                        lista_b.append(0)
            
            lista_r.sort()
            lista_g.sort()
            lista_b.sort()
            # indice exatamente no meio = 7 
            nova_img.putpixel((linha, coluna), (lista_r[7], lista_g[7], lista_b[7]))
    
    return nova_img
            
            
            

if __name__ == "__main__":
    img = Image.open(in_file("Woman.jpg"))
    
    inicio = timeit.default_timer()
    imagem_filto = filtro_mediana(img)
    fim = timeit.default_timer()

    print("Tempo de execução: {}".format(fim - inicio))
    imagem_filto.save(out_file("WomanWithMedianaFilter.png"))