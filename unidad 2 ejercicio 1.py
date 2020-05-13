import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0, 2 * np.pi, 100)
Ya = np.sin(x)
Yb = np.cos(x)

plt.plot(x, Ya)
plt.plot(x, Yb)
plt.show()