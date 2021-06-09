from numpy.lib import math
import librosa.display as lt
from scipy import fftpack
import scipy.io.wavfile
from scipy.fftpack import fft, dct
from numpy import cos, fft as fft
import matplotlib.pyplot as plt
import numpy as np
import time

def mostImportant(npmatrix, n, length):
    # aux = npmatrix.flatten() 
    aux = npmatrix[0]
    npmatrix[0] = 0
    most_imp_index_flatten = np.argpartition(np.absolute(npmatrix), -n)[-n:]
    # print("INDICES MAIS IMPORTANTES")
    # print(most_imp_index_flatten)
    most_imp_index = []
    for i in most_imp_index_flatten:
        most_imp_index.append(i)
    # print("TUPLAS MAIS IMPORTANTES")
    # print(most_imp_index)
    result = np.zeros(length)
    result[0] = aux #npmatrix[0]
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

ini = time.time()

rate,audSaxData=scipy.io.wavfile.read("../input/sax-tenor-a4.wav")
rate,audFluteData=scipy.io.wavfile.read("../input/flute-a4.wav")
rate,audMUSData=scipy.io.wavfile.read("../input/MaisUmaSemana.wav")

# DCT usando função do python
audSaxData_dct = dct(audSaxData)
audFluteData_dct = dct(audFluteData)
audMUSData_dct = dct(audMUSData)

# iDCT usando função do python
# iAudSaxData_dct = fftpack.idct(audSaxData, norm='ortho')
# iAudFluteData_dct = fftpack.idct(audFluteData, norm='ortho')
# iAudMUSData_dct = fftpack.idct(audMUSData, norm='ortho')


# plot dos audios orginais
plt.plot(audSaxData, color='#ff7f00')
plt.title('sax-tenor-a4 Original')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.savefig('./output/sax_wav/sax-tenor-a4_original.png')
# plt.show()

plt.plot(audFluteData, color='#ff7f00')
plt.title('flute-a4 Original')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.savefig('./output/flute_wav/flute-a4_original.png')
# plt.show()

plt.plot(audMUSData, color='#ff7f00')
plt.title('MaisUmaSemana Original')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.savefig('./output/MaisUmaSemana_wav/MaisUmaSemana_original.png')
# plt.show()


# plot dos audios com a DCT do python
plt.plot(audSaxData_dct, color='#ff7f00')
plt.title('sax-tenor-a4 DCT')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.savefig('./output/sax_wav/sax-tenor-a4_dct.png')
# plt.show()

plt.plot(audFluteData_dct, color='#ff7f00')
plt.title('flute-a4 DCT')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.savefig('./output/flute_wav/flute-a4_dct.png')
# plt.show()

plt.plot(audMUSData_dct, color='#ff7f00')
plt.title('MaisUmaSemana DCT')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.savefig('./output/MaisUmaSemana_wav/MaisUmaSemana_dct.png')
# plt.show()

# plot dos audios com a função iDCT do python
# plt.plot(iAudSaxData_dct, color='#ff7f00')
# plt.title('sax-tenor-a4 iDCT')
# plt.xlabel('k')
# plt.ylabel('Amplitude')
# plt.savefig('./output/sax_wav/sax-tenor-a4_idct.png')
# plt.show()

# plt.plot(iAudFluteData_dct, color='#ff7f00')
# plt.title('flute-a4 iDCT')
# plt.xlabel('k')
# plt.ylabel('Amplitude')
# plt.savefig('./output/flute_wav/flute-a4_idct.png')
# plt.show()

# plt.plot(iAudMUSData_dct, color='#ff7f00')
# plt.title('MaisUmaSemana iDCT')
# plt.xlabel('k')
# plt.ylabel('Amplitude')
# plt.savefig('./output/MaisUmaSemana_wav/MaisUmaSemana_idct.png')
# plt.show()


sax_idct = mostImportant(np.asarray(audSaxData_dct), 1024, len(audSaxData))
final = idct(sax_idct.tolist())
final_sax = np.asarray(final).astype(np.uint8)

plt.plot(final_sax, color='#ff7f00')
plt.title('sax-tenor-a4 iDCT')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.savefig('./output/sax_wav/sax-tenor-a4_idct.png')
# plt.show()

flute_idct = mostImportant(np.asarray(audFluteData_dct), 1024, len(audFluteData))
final = idct(flute_idct.tolist())
final_flute = np.asarray(final).astype(np.uint8)

plt.plot(final_flute, color='#ff7f00')
plt.title('flute-a4 iDCT')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.savefig('./output/flute_wav/flute-a4_idct.png')
# plt.show()

MaisUmaSemana_idct = mostImportant(np.asarray(audMUSData_dct), 1024, len(audMUSData))
final = idct(MaisUmaSemana_idct.tolist())
final_MUS = np.asarray(final).astype(np.uint8)

plt.plot(final_MUS, color='#ff7f00')
plt.title('MaisUmaSemana iDCT')
plt.xlabel('k')
plt.ylabel('Amplitude')
plt.savefig('./output/MaisUmaSemana_wav/MaisUmaSemana_idct.png')
# plt.show()

saveSax = audSaxData_dct[0]
saveFlute = audFluteData_dct[0]
saveMaisUmaSemana = audMUSData_dct[0]

scipy.io.wavfile.write("./output/sax_wav/sax-tenor-a4_dct.wav", rate, final_sax.astype(np.int16))
scipy.io.wavfile.write("./output/flute_wav/flute-a4_dct.wav", rate, final_flute.astype(np.int16))
scipy.io.wavfile.write("./output/MaisUmaSemana_wav/MaisUmaSemanadct.wav", rate, final_MUS.astype(np.int16))

# print(rate)
# print(audSaxData)
fim = time.time()
print(f"O NÍVEL DC DE 'sax-tenor-a4' É {saveSax:.4f}")
print(f"O NÍVEL DC DE 'flute-a4' É {saveFlute:.4f}")
print(f"O NÍVEL DC DE 'MaisUmaSemana' É {saveMaisUmaSemana:.4f}")
print(f"O CÓDIGO DEMOROU {fim-ini:.2f} SEGUNDOS")
# print(audData_dct)
# print(iAudData_dct)