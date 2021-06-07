from numpy.lib import math
from scipy import fftpack
import scipy.io.wavfile
from scipy.fftpack import fft, dct
from numpy import fft as fft
import matplotlib.pyplot as plt
import numpy as np
import time

def mostImportant(npmatrix, k, length):
    # aux = npmatrix.flatten()
    #aux[0] = 0
    most_imp_index = np.argpartition(np.absolute(npmatrix), -k)[-k:]
    # print("INDICES MAIS IMPORTANTES")
    # print(most_imp_index_flatten)
    # most_imp_index = []
    # for i in most_imp_index_flatten:
    #     most_imp_index.append(i%length)
    # print("TUPLAS MAIS IMPORTANTES")
    # print(most_imp_index)
    result = np.zeros(length)
    result[0] = npmatrix[0]
    for j in most_imp_index:
        result[j] = npmatrix[j]
        #print(f"VALOR: {npmatrix[j]}")
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

ini = time.time()

rate,audData=scipy.io.wavfile.read("../input/sax-tenor-a4.wav")
audData_dct = dct(audData)

np_idct = mostImportant(np.asarray(audData_dct), 1024, len(audData))
final = dct(np_idct.tolist())
final = np.asarray(final).astype(np.uint8)

save = audData_dct[0]

scipy.io.wavfile.write("sax_dct.wav", rate, final.astype(np.int16))

fim = time.time()

print(rate)
print(final)
print(audData)
print(audData_dct)
print(f"O NÍVEL DC DE É {save}")
print(f"O CÓDIGO DEMOROU {fim-ini:.2f} SEGUNDOS")