# Matplotlib = data ko graph me dikhana
import matplotlib.pyplot as plt

# Data
x=[1,2,3,4,5]
y=[35,50,65,70,85]

# Scatter Plot 
plt.scatter(x,y)
plt.title("Scatter Plot")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.bar(x,y)
plt.title("Bar Chart")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()