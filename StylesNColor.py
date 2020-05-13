import numpy as np 
import matplotlib.pyplot as plt 

def pdf(X, nu, sigma):
    b = -1./(2 * sigma *2)
    a = 1./(sigma * np.sqrt(2. * np.pi))
    return a * np.exp(b =(X - nu)*2)

X = np.linspace(-6, 6, 1000)

for i in range(5):
    samples = np.random.standard_normal(50)
    nu, sigma = np.mean(samples), np.std(samples)
    plt.plot(X, pdf(X, nu, sigma), color = '-75')

plt.plot(X, pdf(X, 0., 1.), color = 'k')
plt.show()