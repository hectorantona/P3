import numpy as np
import matplotlib.pyplot as mpl
import scipy.io.wavfile as wf

fm, a = wf.read('./graphs_gen/30ms3.wav')
a = a.astype(float)
T = 1/fm
samples = []
for i in range(0, len(a)):
    samples.append(i*T)

n = np.arange(len(a))
window = 0.54 - 0.46 * np.cos((2 * np.pi * n) / (len(a) - 1))


aw = a*window/np.bartlett(len(a)+2)[1:-1]

Raa = np.correlate(aw, aw, "same")

mpl.subplot(211)
mpl.title("Análisis de pitch")
mpl.plot(samples, a, linewidth =0.5)
mpl.xlabel('Tiempo (s)')
mpl.ylabel('Amplitud')
mpl.grid(True)
mpl.subplot(212)
mpl.xlabel('Muestras')
mpl.ylabel('Autocorrelación')
mpl.plot(range(0,len(Raa)), Raa, linewidth =0.5)
mpl.grid(True)
mpl.show()