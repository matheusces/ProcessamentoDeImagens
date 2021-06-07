from PIL import Image
import timeit
from filtro_media import filtro_media
from utils import in_file, out_file, correlacao


if __name__ == "__main__":
    img = Image.open(in_file("Woman.jpg"))

    inicio_25x25 = timeit.default_timer()
    imagem_filto_1 = filtro_media(img, (25, 25))
    fim_25x25 = timeit.default_timer()

    inicio_25x1_1x25 = timeit.default_timer()
    imagem_filto_2 = filtro_media(img, (25, 1))
    imagem_filto_2 = filtro_media(imagem_filto_2, (1, 25))
    fim_25x1_1x25 = timeit.default_timer()

    print("Tempo de execução do filtro 25x25: {}".format(fim_25x25 - inicio_25x25))
    imagem_filto_1.save(out_file("WomanWith25x25MediaFilter.png"))

    print("Tempo de execução do filtro 25x1 e depois 1x25: {}".format(fim_25x1_1x25 - inicio_25x1_1x25))
    imagem_filto_2.save(out_file("WomanWith25x1_1x25MedialFilter.png"))