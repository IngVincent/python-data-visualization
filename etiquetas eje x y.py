import numpy as np 
import matplotlib.pyplot as plt 

X= np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X -2.)

plt.title('A polynomial')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.plot(X, Y, c = 'k')
plt.show()