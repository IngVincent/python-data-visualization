import numpy as np 
import matplotlib.pyplot as plt 

women_pop = np.array([5., 30., 45., 22.])
men_pop = np.array([5., 25., 50., 20.])

x = np.range(4)

plt.barh(x, women_pop, color = '.25')
plt.barh(x, -men_pop, color = '.75')
plt.show()