import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 

anim_object1, = plt.plot([], [], '-', lw=2) 
anim_object2, = plt.plot([], [], '-', lw=2)
anim_object3, = plt.plot([], [], '-', lw=2)

xdata1, ydata1 = [], [] 
xdata2, ydata2 = [], [] 
xdata3, ydata3 = [], [] 

ax.set_xlim(0, 7*np.pi) 
ax.set_ylim(-7, 7) 

def update(frame):
    xdata1.append(frame)
    ydata1.append(np.sin(frame+np.pi))
    anim_object1.set_data(xdata1, ydata1) 

    xdata2.append(frame) 
    ydata2.append(np.sin(frame)+4)
    anim_object2.set_data(xdata2, ydata2) 

    xdata3.append(frame) 
    ydata3= np.array(ydata1)+np.array(ydata2)-2
    anim_object3.set_data(xdata3, ydata3) 

ani = FuncAnimation(fig,
                    update, 
                    frames=np.arange(0, 7*np.pi, 0.1),
                    interval=100 
                    )            

  
ani.save('proect_4_task.gif')