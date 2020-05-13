import matplotlib.pyplot as plt

A= [5., 30., 45., 22.]
B= [5., 25., 50., 20.]

X = range(4)
plt.bar(X,A, color ='b')
plt.bar(X, B, color = 'g', bottom = A) #bottom hace que el fin de la barra inferior sea la base de esta barra

plt.show()