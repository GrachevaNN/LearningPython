
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0., 1., 100)
y1 = np.sin(4*np.pi*x)
y2 = np.exp(x) - 1.
y3 = np.cos(4*np.pi*x)

plt.plot(x, y1, x, y2, x, y3, lw = 2, ms = 4)
plt.show()