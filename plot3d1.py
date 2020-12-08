import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

time, x, y, z = np.loadtxt("output1.csv",delimiter=",",usecols=(0,1,2,3),unpack=True)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x,y,z,color="red")
plt.show()
