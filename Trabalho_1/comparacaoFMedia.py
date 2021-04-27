from PIL import Image
import timeit
from filtro_media import filtro_media
from utils import in_file, out_file, correlacao       
            

if __name__ == "__main__":
    img = Image.open(in_file("Woman.jpg"))

    MEDIA_25x25 = [
                1/15, 1/15, 1/15, 1/15, 1/15, 1/15, 1/15, 1/15, 1/15, 1/15, 
                1/15, 1/15, 1/15, 1/15, 1/15,
                1/15, 1/15, 1/15, 1/15, 1/15
            ]
    
    inicio = timeit.default_timer()
    imagem_filto = filtro_media(img)
    fim = timeit.default_timer()

    print("Tempo de execução: {}".format(fim - inicio))
    imagem_filto.save(out_file("WomanWithMediaFilter.png"))