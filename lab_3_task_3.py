import numpy as np
from lab_3_task_1 import yskorenie_svobodnogo_padeniya as g

x0 = 1
y0 = 3
v0x = 13
t = np.arange(0, 5, 0.01)

x = x0 + v0x*t 
y = y0 + v0x*t - (g*t**2)/2
print(x, y)