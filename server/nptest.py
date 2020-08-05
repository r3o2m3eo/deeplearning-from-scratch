import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
mpl.use('Agg')

x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(x)
y2 = np.cos(x)

fig = plt.figure()
plt.plot(x, y)
plt.plot(x, y2)

plt.xlabel("x")
plt.ylabel("y")

fig.savefig('./img.png')
