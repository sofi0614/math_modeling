import matplotlib.pyplot as plt
import numpy as np

plt.arrow(0, 0, 4, 4, width=0.02)
plt.savefig('vektor.png')
plt.close()

x, y = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))

U = 1
V = -1
plt.quiver(x, y, U, V)
plt.title('Векторная точка скоростей, V = {1; -1}, м/с')
plt.xlabel('Координата x, м')
plt.ylabel('Координата y, м')
plt.savefig('vector_field_1.png')
plt.close()

U = x/np.sqrt(x**2 + y**2)
V = y/np.sqrt(x**2 + y**2)
plt.quiver(x, y, U, V)
plt.title('Векторная точка скоростей, V = {1; -1}, м/с')
plt.xlabel('Координата x, м')
plt.ylabel('Координата y, м')
plt.savefig('vector_field_2.png')
plt.close()

U = -y/np.sqrt(x**2 + y**2)
V = x/np.sqrt(x**2 + y**2)
plt.quiver(x, y, U, V)
plt.title('Векторная точка скоростей, V = {1; -1}, м/с')
plt.xlabel('Координата x, м')
plt.ylabel('Координата y, м')
plt.savefig('vector_field_3.png')
plt.close()

U = -y/np.sqrt(x**2 + y**2)+y
V = x/np.sqrt(x**2 + y**2)
plt.quiver(x, y, U, V)
plt.title('Векторная точка скоростей, V = {1; -1}, м/с')
plt.xlabel('Координата x, м')
plt.ylabel('Координата y, м')
plt.savefig('vector_field_4.png')
plt.close()