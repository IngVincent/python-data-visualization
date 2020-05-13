import numpy as np 
import matplotlib.pyplot as plt 

data= np.random.standard_normal((100,2))

plt.scatter(data[:,0], data[:,1], color = '.95', edgecolor= '.10')
plt.show()