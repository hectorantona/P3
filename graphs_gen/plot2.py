import numpy as np
import matplotlib.pyplot as mpl
import scipy.io.wavfile as wf

pot = np.loadtxt("./graphs_gen/pot.txt", dtype=float)
r1norm = np.loadtxt("./graphs_gen/r1norm.txt", dtype=float)
rMaxnorm = np.loadtxt("./graphs_gen/rMaxnorm.txt", dtype=float)
pitch = np.loadtxt("./graphs_gen/pitch.txt", dtype=float)

fm = 20000
time = np.arange(0,len(pot)).astype(float)
time = time/fm

mpl.subplot(411)
mpl.title("Parámetros de la señal")
mpl.plot(time, pot, linewidth =0.5)
mpl.xlabel('Tiempo (s)')
mpl.ylabel('Amplitud')
mpl.grid(True)
mpl.subplot(412)
mpl.xlabel('Tiempo (s)')
mpl.ylabel('r1norm')
mpl.plot(time, r1norm, linewidth =0.5)
mpl.grid(True)
mpl.subplot(413)
mpl.xlabel('Tiempo (s)')
mpl.ylabel('rmaxnorm')
mpl.plot(time, rMaxnorm, linewidth =0.5)
mpl.grid(True)
mpl.subplot(414)
mpl.xlabel('Tiempo (s)')
mpl.ylabel('pitch (Hz)')
mpl.plot(time, pitch, linewidth =0.5)
mpl.grid(True)
mpl.show()