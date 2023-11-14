import numpy as np

h = 100
a = np.pi/3
b = 30
g = 9.8

d =(g*h*np.tan(b)**2)
n =(2*np.cos(a)**2*(1-np.tan(b)*np.tan(a)))
v = (d/n)**1/2
print(v)