import math

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
    pi_value = math.pi

    parteRepetida = pi_value/big_n
    parteRepetida2 = parteRepetida/2

    for k in range(0, big_n):
        if k == 0:
            xk = 0
            for n in range(0, big_n):
                xk += lista[n]
            amplitudes.append(cte*ck*xk)
        else:
            ck = 1
            xk = 0
            parte1Arg = k*parteRepetida
            parte2Arg = k*parteRepetida2

            for n in range(0, big_n):
                xk += lista[n]*math.cos((parte1Arg*n + parte2Arg))
            amplitudes.append(cte*xk)
    return amplitudes