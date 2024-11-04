import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = np.loadtxt(fname=signal_filepath, skiprows=2, delimiter=',')

og_signal = signal[:,1]

# Show plot of Signal
plt.plot(og_signal,  label="Original Signal")
plt.xlabel('Index')
plt.title("Original Signal")
plt.show()

## YOUR CODE HERE ##


"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##
dif = np.diff(signal[:,1])

# Show plot of diff
plt.plot(dif,  label="Differential")
plt.xlabel('Index')
plt.title("Differential")
plt.show()

"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
square = np.square(dif)

# Show plot of square
plt.plot(square,  label="Square")
plt.xlabel('Index')
plt.title("Squared")
plt.show()

"""
Step 5: Pass a moving filter over your data
"""

## YOUR CODE HERE
conv = [1,1,1,1,1,1,1,1]
avg = np.convolve(square, conv, mode='valid')

# Show plot of moving average
plt.plot(avg,  label="Moving Average")
plt.xlabel('Index')
plt.title("Moving Average")
plt.show()



# make a plot of the results. Can change the plot() parameter below to show different intermediate signals

