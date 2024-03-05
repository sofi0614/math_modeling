from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
import numpy as np 

def circle_move(R, time):
    R = 0.02 * time
    alpha = np.arange(0, 3*np.pi, 0.1)
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x, y

def animate(i):
    ball.set_data(circle_move(R=0.5, time = i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='r', label ='Ball')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30
                        )
    
    ani.save('animation_task2.gif') 