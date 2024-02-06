import matplotlib.pyplot as plt 
import numpy as np

def giperbola_plotter(k = 3):

    x = np.arange (-13, -0.01, 0.01)
    y = k/x

    plt.plot(x, y)
    plt. savefig('fig_6.png')

if __name__ == '__main__':
    giperbola_plotter()