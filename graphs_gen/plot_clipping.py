import numpy as np
import matplotlib.pyplot as mpl
import scipy.io.wavfile as wf

fm, a = wf.read('./graphs_gen/30ms3.wav')
a = a.astype(float)
T = 1/fm
samples = []
for i in range(0, len(a)):
    samples.append(i*T)

cl_th = max(a) * 0.3

clip = np.array(a)
for i in range(len(clip)):
    if clip[i] >= cl_th:
        clip[i] -= cl_th
    else:
        if clip[i] <= -cl_th:
            clip[i] += cl_th
        else:
            clip[i] = 0

mpl.subplot(211)
mpl.title("Center Clipping")
mpl.plot(samples, a, linewidth =0.5)
mpl.xlabel('Tiempo (s)')
mpl.ylabel('Amplitud')
mpl.grid(True)
mpl.subplot(212)
mpl.xlabel('Tiempo (s)')
mpl.ylabel('Amplitud')
mpl.plot(samples, clip, linewidth =0.5)
mpl.grid(True)
mpl.show()
