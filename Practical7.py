# Customization = graph ko decorate karna (color, title, labels, grid)
import matplotlib.pyplot as plt 

x= [1,2,3,4,5]
y =[35,50,65,70,85]
plt.plot(x,y, color = 'red' , marker='o' , linestyle= '--')

plt.title("Customized Line Chart")
plt.xlabel("Hours")
plt.ylabel("Marks")

plt.grid(True)
plt.show()