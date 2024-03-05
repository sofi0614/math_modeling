import matplotlib.pyplot as plt
import numpy as np

def cicloida (a=3):
    t = np.arange(0, 8, 0.1)

    x = a * (t - np.sin(t))
    y = a * (1 - np.cos(t))

    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig_task1.png')

if __name__ == '__main__':
    cicloida()
