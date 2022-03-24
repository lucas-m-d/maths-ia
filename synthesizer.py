# requires python 3.8.5 or greater
# requires numpy and scipy to be installed

import numpy as np
import scipy.io.wavfile
import csv

sample_freq = 44100
length = 3
datapoints = np.arange(0, length, 1/sample_freq)
fundamental = 259.4117647058824 # change to acheive desired fundamental
with open('out.csv', newline='') as out:
    rows = []
    reader = csv.reader(out)
    for row in reader:
        rows.append(row)
    Fk = [float(i) for i in rows[0]]
    Ak = [float(i) for i in rows[1]]
    Pk = [float(i) for i in rows[2]]

fundamental_ratio = fundamental/Fk[0]
Fk = np.multiply(Fk, fundamental_ratio)
coefficient_len = len(Fk)
waves = []
for i in range(coefficient_len):
    cos_input = np.multiply(datapoints, 2*np.pi*Fk[i])
    cos_input += Pk[i]
    cos = np.cos(cos_input)
    cos = np.multiply(cos, Ak[i])
    waves.append(cos)

output = waves[0].copy()

for i in range(1, coefficient_len):
    output = np.add(output, waves[i])

output = np.multiply(output, 1)

scipy.io.wavfile.write("clarinet_synth_1.NIST", 44100, output)
