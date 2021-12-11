import numpy as np
import pandas as pd
import neurokit2 as nk
import struct

ecg1 = nk.ecg_simulate(duration=7, sampling_rate=44100, heart_rate=77)
ecg2 = nk.ecg_simulate(duration=9, sampling_rate=44100, heart_rate=66)
ecg3 = nk.ecg_simulate(duration=15, sampling_rate=44100, heart_rate=55)
ecg4 = nk.ecg_simulate(duration=9, sampling_rate=44100, heart_rate=88)
ecg5 = nk.ecg_simulate(duration=7, sampling_rate=44100, heart_rate=44)
ecg6 = nk.ecg_simulate(duration=8, sampling_rate=44100, heart_rate=99)
ecg7 = nk.ecg_simulate(duration=5, sampling_rate=44100, heart_rate=50)

f = open('ECG WAV Dataset/50.wav', 'wb')
for i in ecg1:
    f.write(struct.pack('b', int(i)))
for i in ecg2:
    f.write(struct.pack('b', int(i)))
for i in ecg3:
    f.write(struct.pack('b', int(i)))
for i in ecg4:
    f.write(struct.pack('b', int(i)))
for i in ecg5:
    f.write(struct.pack('b', int(i)))
for i in ecg6:
    f.write(struct.pack('b', int(i)))
for i in ecg7:
    f.write(struct.pack('b', int(i)))
f.close()

signals1, info = nk.ecg_process(ecg1, sampling_rate=44100)
nk.ecg_plot(signals1, sampling_rate=44100, show_type='default')

signals2, info = nk.ecg_process(ecg2, sampling_rate=44100)
nk.ecg_plot(signals2, sampling_rate=44100, show_type='default')

signals3, info = nk.ecg_process(ecg3, sampling_rate=44100)
nk.ecg_plot(signals3, sampling_rate=44100, show_type='default')

signals4, info = nk.ecg_process(ecg4, sampling_rate=44100)
nk.ecg_plot(signals4, sampling_rate=44100, show_type='default')

signals5, info = nk.ecg_process(ecg5, sampling_rate=44100)
nk.ecg_plot(signals5, sampling_rate=44100, show_type='default')

signals6, info = nk.ecg_process(ecg6, sampling_rate=44100)
nk.ecg_plot(signals6, sampling_rate=44100, show_type='default')

signals7, info = nk.ecg_process(ecg7, sampling_rate=44100)
nk.ecg_plot(signals7, sampling_rate=44100, show_type='default')