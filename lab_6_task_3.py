import matplotlib.pyplot as plt 
import numpy as np 

def elips_plotter(a = 4, b = 2):
    x = np.arange(-12, 12, 0.01)
    y = np.arange(-12, 12, 0.01)

    X, Y = np.meshgrid(x, y)

    fxy = X**2/a**2 + Y**2/b**2

    plt.contour(X, Y, fxy, levels = [1])
    plt.axis('equal')

    plt.savefig('fig_7.png')

if __name__ == '__main__':
    elips_plotter()