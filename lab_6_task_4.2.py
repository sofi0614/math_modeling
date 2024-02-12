import matplotlib.pyplot as plt
import numpy as np

def spiral_plotter(k = 0.1):

    f = np.arange(0, 8*np.pi, 0.01)
    r = k*f

    x = r*np.cos(f)
    y = r*np.sin(f)

    plt.plot(x, y)
    plt.savefig('fig_task4_2.png')

if __name__ == '__main__':
    spiral_plotter()