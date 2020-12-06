
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 21)
y = np.linspace(0, 20, 21)
X, Y = np.meshgrid(x, y)
z = X * np.exp(-0.1 * (X - Y) **2)
v = np.linspace(-0.5, 0.5, 21)

# Контурный график с подписанными изолиниями, цвет линий - красныый
#cs = plt.contour(x, y, z, v, colors = 'r')
#plt.clabel(cs, inline = 'True', fontsize = 10)

# Контурный график с подписанными изолиниями, с заливкой областей
#plt.contourf(x, y, z, v)
#plt.colorbar()

# Контурный график с выбором палитры для заливки областей
plt.pcolor(x, y, z, vmin = 0.025, vmax = 0.975, cmap = 'gray')
plt.colorbar(orientation = 'horizontal')
plt.show()


