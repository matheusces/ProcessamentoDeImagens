import os;

INPUT_DIR = "Trabalho_1/input"
OUTPUT_DIR = "Trabalho_1/output"

def in_file(filename):
    return os.path.join(INPUT_DIR, filename)


def out_file(filename):
    return os.path.join(OUTPUT_DIR, filename)


def correlacao(imagem, filtro, dimensao_filtro, tupla_pixel):
    w, h = imagem.size

    linha = tupla_pixel[0]
    coluna = tupla_pixel[1]
    var_linha = int(dimensao_filtro[0]/2) # variante da linha do inicio ao fim
    var_coluna = int(dimensao_filtro[1]/2) # variante da coluna do inicio ao fim
    
    soma_r = 0
    soma_g = 0
    soma_b = 0
    i = 0

    # for que vai percorrer a vizinhança do píxel de acordo com a dimensão do filtro
    for m in range(linha-var_linha, linha+var_linha+1):
        for n in range(coluna-var_coluna, coluna+var_coluna+1):
            if m >= 0 and m < w and n >= 0 and n < h:
                pxl = imagem.getpixel((m,n))

                soma_r += pxl[0] * filtro[i]
                soma_g += pxl[1] * filtro[i]
                soma_b += pxl[2] * filtro[i]
            
            i+=1
    
    return (soma_r, soma_g, soma_b)
                

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

                soma += pxl * filtro.getpixel((i, j))
            j+=1
        i+=1
    
    return soma