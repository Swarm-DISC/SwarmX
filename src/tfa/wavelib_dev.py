# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 15:22:24 2022

@author: constantinos@noa.gr
"""

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# t, dt = np.linspace(0, 1, 2000, retstep=True)
N = 1000
dt = 1
t = np.arange(0, N-1)
fs = 1/dt
w0 = 6

fwl = 4*np.pi/(w0 + np.sqrt(2 + w0**2))
width_param = (2*np.pi)/(w0*fs)
print([fwl, width_param])

# sig = np.cos(2*np.pi*(50 + 10*t)*t) + np.sin(40*np.pi*t)
sig = np.cos(2*np.pi*t/(10*dt))

freq = np.linspace(0, fs/2, 100)

widths = w0*fs / (2*freq*np.pi)

cwtm = signal.cwt(sig, signal.morlet2, widths, w=w0)

plt.figure(1)
plt.pcolormesh(t, freq, np.abs(cwtm), cmap='viridis', shading='gouraud')

plt.figure(2)
plt.plot(freq, np.abs(cwtm[:,int(N/2)]))
