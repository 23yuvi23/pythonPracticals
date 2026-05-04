# SciPy = advanced math & scientific operations (NumPy ka upgrade)
# Function	Library
# Mean	     NumPy
# Median	 NumPy
# Histogram	 Matplotlib
# Mode	     SciPy

import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt

# data
data = np.array([10,20,20,30,40,50])

print ("Data:" , data)

# Mean
mean = np.mean(data)
print("Mean:",mean)

# Median
median = np.median(data)
print("Median:",median)

# Mode
mode = stats.mode(data)
print("Mode",mode.mode)

# Visualization (Histogram)
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
