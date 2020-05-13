import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.tri as tri 

data = np.random.rand(100, 2)
trinagles = tri.Triangulation(data[:,0], data[:,1])

plt.triplot(trinagles)
plt.show()
