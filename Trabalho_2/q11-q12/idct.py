import math
import numpy
from dct import pegarColuna

def idct(lista):

    valores = []
    big_n = len(lista)
    cte = (2 / big_n) ** 0.5
    ck = 1
    pi_value = math.pi

    parteRepetida = pi_value / (2*big_n)

    for n in range(0, big_n):
        xn = 0
        argumento = (2*n + 1) * parteRepetida
        for k in range(0, big_n):
            if k == 0:
                ck = 0.5 ** 0.5
            xn += (ck * lista[k] * math.cos(argumento * k))
            ck = 1
        valores.append(cte * xn)

    return valores

def idct2d(lista):
    lista2 = lista.copy()
    aux1 = []
    for i in range(len(lista)):
        aux1.append(idct(lista[i]))

    for j in range(len(aux1[0])):
        aux2 = []
        aux2 = idct(pegarColuna(aux1, j))
        for k in range(len(aux2)):
            lista2[k][j] = aux2[k]

    return lista2
