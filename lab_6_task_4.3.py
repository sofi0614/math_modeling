import matplotlib.pyplot as plt
import numpy as np

def spiral_zhezl(k = 1):

    f = np.arange(0.05, 8*np.pi, 0.01)
    r = k / f**(1/2)

    x = r*np.cos(f)
    y = r*np.sin(f)

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('fig_task4_3.png')


if __name__ == '__main__':
    spiral_zhezl()