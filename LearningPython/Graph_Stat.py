from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

def z_function(x, y):
    return 450.56 - 0.048 * x + 4.6 * y + 0.0003 * x ** 2 - 0.0718 * y ** 2

x = np.linspace(0, 500, 50)
y = np.linspace(0, 64, 32)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

# построение поверхности,
# с указанием шага сетки на поверхности (rstride, cstride),
# цветовой карты (cmap) и цвета границы на поверхности (edgecolor)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet', edgecolor='k')
#ax.contourf(X, Y, Z, 100, cmap='jet')

# установка белого фона сетки
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

# подписи (заголовки) осей,
# с указанием размера и цвета шрифта
# текст в $$ - текст в формате LaTex
ax.set_xlabel('$X$', fontsize = 15, color = 'black')
ax.set_ylabel('$Z$', fontsize = 15, color = 'black')
ax.set_zlabel('$T_{GPU}, ms$', fontsize = 15, color = 'black')

#ax.contour(Z)

# создание цветовой шкалы (colorbar)
m = cm.ScalarMappable(cmap = 'jet') 
m.set_array(Z) 
plt.colorbar(m,shrink = 0.5) 

#plt.savefig('Stat_3D.svg', fmt='svg')

plt.show()
