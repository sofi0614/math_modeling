import matplotlib.pyplot as plt
import numpy as np
import random 

fig, ax = plt.subplots()
N = 1000
x, y = np.zeros(N), np.zeros(N)
for i in range(N):
    x[i]=random.uniform(0, 1)
    y[i]=random.uniform(0, 1)

scalar_field = 50*np.sqrt(x**2 + y**2)

sc_plot = ax.scatter(x, y,c = scalar_field)
ax.set_xlabel('Координата x, м')
ax.set_xlabel('Координата y, м')

cbar = fig.colorbar(sc_plot)
cbar.set_label('Сколярное поле температуры, C')

plt.savefig("dich.png")