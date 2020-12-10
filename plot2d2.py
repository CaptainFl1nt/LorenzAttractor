import numpy as np
import matplotlib.pyplot as plt

time, x, y, z = np.loadtxt("output_26.csv",delimiter=",",usecols=(0,1,2,3),unpack=True)
time1, x1, y1, z1 = np.loadtxt("output_22.csv",delimiter=",",usecols=(0,1,2,3),unpack=True)

fig, ax = plt.subplots(3)
fig.subplots_adjust(hspace=0)
t = 6000
w = 0.75
ax[0].plot(time[0:t],x[0:t],color="red",linewidth=w)
ax[1].plot(time[0:t],y[0:t],color="red",linewidth=w)
ax[2].plot(time[0:t],z[0:t],color="red",linewidth=w)
ax[0].plot(time1[0:t],x1[0:t],color="blue",linewidth=w)
ax[1].plot(time1[0:t],y1[0:t],color="blue",linewidth=w)
ax[2].plot(time1[0:t],z1[0:t],color="blue",linewidth=w)

ax[0].set_ylabel(r"$x$")
ax[1].set_ylabel(r"$y$")
ax[2].set_ylabel(r"$z$")
ax[2].set_xlabel("Time")

plt.show()
