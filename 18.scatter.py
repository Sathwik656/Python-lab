import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
time = np.random.randint(0,25,size=20)
temperature = np.random.randint(20,31,size=20)

plt.scatter(time,temperature,color='red',edgecolors='black',label='Temprature vs Time',marker='o')

plt.title("Temprature vs Time")
plt.xlabel("Time (hours)")
plt.ylabel("Temprature (C)")
plt.grid()
plt.legend()
plt.show()

plt.scatter(time,temperature,c=temperature,cmap='virdis',edgecolor='black',label="Temprature vs Time")
plt.colorbar(label="Temprature (C)")
plt.title("Scatter plot with color and size variation")
plt.xlabel("Tome (hours)")
plt.ylabel("Tempratire (C)")
plt.grid(True)
plt.legend()
plt.show()