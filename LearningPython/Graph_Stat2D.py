from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import math

x = np.linspace(-2*math.pi, 2*math.pi, 100)
y = np.sin(x)

# подписи (заголовки) осей,
# с указанием размера и цвета шрифта
# текст в $$ - текст в формате LaTex
plt.xlabel('$k$', fontsize = 15, color = 'black')
plt.ylabel('$Y$', fontsize = 15, color = 'black')

plt.plot(x, y, linestyle = '-.', linewidth = 6, color = 'g',  label = 'sin(x)')
plt.legend(loc='upper right', frameon=False)


plt.show()
