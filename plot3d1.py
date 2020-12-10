import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
s = 10
b = 8.0/3.0
r = 28
time, x, y, z = np.loadtxt("output_26.csv",delimiter=",",usecols=(0,1,2,3),unpack=True)
#time2, x2, y2, z2 = np.loadtxt("output5.csv",delimiter=",",usecols=(0,1,2,3),unpack=True)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$z$")

ax.plot(x,y,z,color="red",linewidth=0.25)
#ax.plot(x2,y2,z2,color="blue",linewidth=0.5)

X1 = np.array([math.sqrt(b*(r-1))])
Y1 = np.array(X1)
Z1 = np.array([r-1])
X2 = -X1
Y2 = -Y1

ax.scatter(X1,Y1,Z1,color="purple")
ax.scatter(X2,Y2,Z1,color="blue")
ax.scatter([0],[0],[0],color="green")
plt.show()
