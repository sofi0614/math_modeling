import matplotlib.pyplot as plt
import numpy as np

def spiral_rose(k = 5):

    f = np.arange(0.05, 8*np.pi, 0.01)
    r = np.sin(k*f)

    x = r*np.cos(f)
    y = r*np.sin(f)

    plt.plot(x, y)
    plt.savefig('fig_task4_4.png')


if __name__ == '__main__':
    spiral_rose()