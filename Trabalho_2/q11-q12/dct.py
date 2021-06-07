import math
from PIL import Image
import numpy
import time

def pegarColuna(matrix, col):
    result = []
    for i in range(len(matrix)):
        result.append(matrix[i][col])
    return result

def dct(lista):
    amplitudes = []
    big_n = len(lista)
    cte = (2/big_n)**0.5
    ck = 0.5**0.5
    pi_value = 3.14159

    parteRepetida = pi_value/big_n
    parteRepetida2 = parteRepetida/2

    for k in range(0, big_n):
        if k == 0:
            xk = 0
            for n in range(0, big_n):
                xk += lista[n]
            amplitudes.append(cte*ck*xk)
        else:
            xk = 0
            parte1Arg = k*parteRepetida
            parte2Arg = k*parteRepetida2

            for n in range(0, big_n):
                xk += (lista[n]*math.cos((parte1Arg*n) + parte2Arg))
            amplitudes.append(cte*xk)
    return amplitudes


def dct2d(imagem):
    img_arr = numpy.asarray(imagem)
    matrix = img_arr.tolist()

    aux1 = []
    for i in range(len(matrix)):
        aux1.append(dct(matrix[i]))

    for j in range(len(aux1[0])):
        aux2 = []
        aux2 = dct(pegarColuna(aux1, j))
        for k in range(len(aux2)):
            matrix[k][j] = aux2[k]

    return matrix




##TESTE COM A FUNÇÃO DO SCIPY
#dctpython = fft.dctn(numpy.asarray(im), norm='ortho')
#save2 = dctpython[0][0]
#print(f"O NÍVEL DC DE ACORDO COM A FUNÇÃO DO PYTHON É {save2}")
#for i in range(0,5):
#    print(f"{i+1}° valor da DCT DO PYTHON: {dctpython[0][i]}")


