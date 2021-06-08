import matplotlib.pyplot as plt
import numpy
import timeit
import librosa
import os
from scipy.io import wavfile
from scipy import fft
import librosa.display as ld
from utils import dct
from pydub import AudioSegment

AudioSegment.from_wav("sax.wav").export("sax2_2.mp3", format="mp3", bitrate="128k")
# AudioSegment.from_wav("MaisUmaSemana.wav").export("MUS2_2.mp3", format="mp3", bitrate="128k")
path_name = os.getcwd() + '/sax2_2.mp3'
# path_name = os.getcwd() + '/MUS2_2.mp3'


plt.rcParams.update({'font.size': 16})
data, fs = librosa.load(path_name)

print(f"Tamanho do arquivo aberto com librosa {len(data)}")

plt.figure(figsize=(10, 6))
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

ld.waveplot(data, sr=fs)
plt.show()

# data = fft.dct(data)
# data = numpy.abs(data)
# dc = data[0]
# print(f"O NÍVEL DC DE ACORDO COM A MINHA FUNÇÃO É {dc}")
# data[0] = 0
# plt.figure(figsize=(10, 6))
# plt.xlabel("Time [s]")
# plt.ylabel("Amplitude [Hz]")
# ld.waveplot(data, sr=fs)
# plt.show()

temp_ini = timeit.default_timer()
data = dct(data)
temp_fim = timeit.default_timer()
dc = data[0]
print(f"O NÍVEL DC DE ACORDO COM A MINHA FUNÇÃO É {dc}")
print(f"Tempo de execução da dct é {temp_fim-temp_ini}")
data[0] = 0
data = numpy.array(data)
data = numpy.abs(data)
plt.figure(figsize=(10, 6))
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [Hz]")
ld.waveplot(data, sr=fs)
plt.show()

wavfile.write(filename="sax2.2_dct.mp3", rate=fs, data=data)
# wavfile.write(filename="MUS2_dct.mp3", rate=fs, data=data)