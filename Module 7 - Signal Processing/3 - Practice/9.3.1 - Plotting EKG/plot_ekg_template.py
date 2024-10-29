import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

data = np.loadtxt(fname=path, skiprows=2, delimiter=',')

# save each vector as own variable
ekg_time = data[:,0]
ekg_MLII = data[:,1]
ekg_V1 = data[:,2]

dif = np.diff(ekg_MLII)
square = np.square(dif)

conv = [1,1,1,1,1,1]
avg = np.convolve(square, conv)

# use matplot lib to generate a single
fig, ax = plt.subplots()
ax.plot(ekg_time,ekg_V1)
plt.show()
