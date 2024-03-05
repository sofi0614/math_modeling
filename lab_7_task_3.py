import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 

anim_object, = plt.plot([], [], '-', lw=2) 

xdata, ydata = [], [] 

ax.set_xlim(-5, 5) 
ax.set_ylim(-5, 5) 

def update(t):
    xdata.append(np.sin(t) * (np.e**np.cos(t) - 2 * np.cos(4*t) + np.sin**5 * (t/12)))
    ydata.append(np.cos(t) * (np.e**np.cos(t) - 2 * np.cos(4*t) + np.sin**5 * (t/12)))
    anim_object.set_data(xdata, ydata) 
    return anim_object,

ani = FuncAnimation(fig,
                    update, 
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=100 
                    )            

ani.save('animation_task_3.gif')