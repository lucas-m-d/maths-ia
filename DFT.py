# Lucas Dick's Maths IA
# Requires Python 3.8.5 or greater, numpy, scipy and matplotlib to be installed
import matplotlib.pyplot as plt
import csv
import scipy.linalg as linalg
import numpy as np

np.set_printoptions(formatter={'float_kind': '{:f}'.format})

# import pandas
SAMPLE_RATE = 44100
with open("real-data-24-1.csv", newline='') as data:
    starting_data = list(csv.reader(data))
    # del starting_data[0]
    starting_data = [float(i[0]) for i in starting_data]
    sample_num = len(starting_data)

T = sample_num/SAMPLE_RATE

dft_matrix = linalg.dft(sample_num)  # creates DFT matrix
complex_data = starting_data @ dft_matrix  # multiply matrices
complex_data = [i for i in complex_data]

data_arguments = [np.angle(i) for i in complex_data]
data_absolute = [2*np.abs(complex_data[i]) / sample_num
                 for i in range(sample_num)]

plt.plot(np.arange(0, SAMPLE_RATE//2, SAMPLE_RATE/sample_num),
         data_absolute[:sample_num//2])
plt.grid(color='gray', linestyle='-')

notable_waves = [[SAMPLE_RATE*i/sample_num, data_absolute[i], data_arguments[i]]
                 for i in range(sample_num) if data_absolute[i] > 0.003 and i < SAMPLE_RATE//2]

with open("out.csv", 'w', newline='') as out:
    writer = csv.writer(out)
    writer.writerow([i[0] for i in notable_waves])
    writer.writerow([i[1] for i in notable_waves])
    writer.writerow([i[2] for i in notable_waves])
print([i[0] for i in notable_waves])
print([i[1] for i in notable_waves])
print([i[2] for i in notable_waves])

# display waves
'''
values = np.arange(0, T, SAMPLE_RATE)
fourier_waves = [np.cos(2*np.pi*i*values + data_arguments[i])
                 for i in range(sample_num//2)]

plt.plot(values, fourier_waves[1] + fourier_waves[2])
plt.grid(True)
plt.axhline(y=0, color='k')
plt.show()
'''
plt.show()
