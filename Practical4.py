#  NumPy = fast numerical operations (arrays pe kaam)
import numpy as np

#Create array 
arr = np.array([10,20,30,40,50,60])

print("Array",arr)

#Basic operations 
print("\nsum",np.sum(arr))
print("Mean",np.mean(arr))
print("Max",np.max(arr))
print("Min",np.min(arr))

# Create arrays
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Basic operations
print("\nSum of arr1:", np.sum(arr1))
print("Mean of arr1:", np.mean(arr1))

# Array addition
print("\nAddition:", arr1 + arr2)

# Multiplication
print("Multiplication:", arr1 * arr2)

# Max and Min
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))