import numpy as np
import matplotlib.pyplot as mpl
import scipy.io.wavfile as wf

f0 = np.loadtxt("./graphs_gen/sb014.f0", dtype=float)
f0ref = np.loadtxt("./graphs_gen/sb014.txt", dtype=float)

fm = 20000
time = np.arange(0,len(f0)).astype(float)
time = time/fm

mpl.subplot(211)
mpl.title("Parámetros de la señal")
mpl.plot(time, f0, linewidth =0.5)
mpl.xlabel('Tiempo (s)')
mpl.ylabel('pitch calculado (Hz)')
mpl.grid(True)
mpl.subplot(212)
mpl.xlabel('Tiempo (s)')
mpl.ylabel('pitch wavesurfer (Hz)')
mpl.plot(time, f0ref, linewidth =0.5)
mpl.grid(True)
mpl.show()