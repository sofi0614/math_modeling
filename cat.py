import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom
import h5py

img = plt.imread('cat.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

t0 = np.linspace(np.pi + np.pi/20, np.pi/2 - np.pi/10, 100)
x0 = 1150 + 850 * np.cos(t0)
y0 = 900 - 800 * np.sin(t0)
ax.plot(x0, y0, '-', lw=5, color = 'm')

t1 = np.linspace(2 * np.pi, 7 * np.pi/4, 100)
x1 = 1210 + 200 * np.cos(t1)
y1 = 150 - 500 * np.sin(t1)
ax.plot(x1, y1, '-', lw=5, color = 'm')

x = np.append(x0, x1)
y = np.append(y0, y1)

t2 = np.linspace(2 * np.pi, 3 * np.pi/2, 100)
x2 = 600 + 750 * np.cos(t2)
y2 = 500 - 700 * np.sin(t2)
ax.plot(x2, y2, '-', lw=5, color = 'm')

x = np.append(x, x2)
y = np.append(y, y2)

t3 = np.linspace(3 * np.pi/2, np.pi, 100)
x3 = 600 + 290 * np.cos(t3)
y3 = 1000 - 200 * np.sin(t3)
ax.plot(x3, y3, '-', lw=5, color = 'm')

x = np.append(x, x2)
y = np.append(y, y3)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0) 
figure_spline_part_manual = np.arange(0, 0.5, 0.01) 
spline_curve = interpolate.splev(figure_spline_part, spline_coords) 
 
curve_coords = [] 
for i in range(len(spline_curve[0])): 
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]]) 
 
polygon = geom.Polygon(curve_coords) 
points_number_per_side = 500 
x_pictures_limits = [0, 1600] 
y_pictures_limits = [1100, 0] 
points_coords = []

for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_func = intensity * np.exp(- dec_rate[0]*x**2 - dec_rate[1]*y**2) 
    return scalar_func

intensity_centerums_x = [600, 400, 380, 300, 700, 900, 1100, 1200, 1300, 1400, 1400, 1400, 1100, 900, 800]
intensity_centerums_y = [400, 800, 500, 1000, 1000, 1050, 1100, 900, 700, 600, 300, 200, 100, 200, 300]
intensity_values = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

def scalar_function(x, y, int_cen_x, int_cen_y, int_vel):
    scalar_field = 0.0
    for i in range(0, len(int_cen_x)):
        scalar_field += int_vel[i] * bell_function(x-int_cen_x[i], y-int_cen_y[i], 0.030, [0.000009, 0.000009])
    return scalar_field

scalar_fields = []
for i in range(0, len(x_p)):
    calculate = scalar_function(x_p[i], y_p[i], intensity_centerums_x, 
                                intensity_centerums_y, intensity_values)
    scalar_fields.append(calculate)


float_type = np.float64
int_type = np.int32

picture_size_x = max(x_pictures_limits)-min(x_pictures_limits)
picture_size_y = max(y_pictures_limits)-min(y_pictures_limits)
picture_size = max(picture_size_x, picture_size_y)
box_size = 100*picture_size

gas_part_num = len(x_p)
gas_coords = np.zeros([gas_part_num, 3], dtype=float_type)
gas_vel= np.zeros([gas_part_num, 3], dtype=float_type)

gas_masses = np.ones(gas_part_num, dtype=float_type)

for i in range(len(x_p)):
    gas_coords[i,0] = x_p[i]/picture_size + box_size/2
    gas_coords[i][1] = y_p[i]/picture_size + box_size/2
    gas_vel[i][0] = float_type(0.001)
    gas_vel[i][0] = float_type(0)

IC = h5py.File('IChorse.hdf5', 'w')
header = IC.create_group('Header')
part0 = IC.create_group('PartType0')
header.attrs.create("BoxSize", box_size)
part0.create_dataset('ParticleIDs', data=np.arange(0, gas_part_num))
part0.create_dataset('Coordinates', data = gas_coords)
part0.create_dataset('Velocities', data = gas_vel)
part0.create_dataset('Masses', data = gas_masses)
IC.close()

fig, ax = plt.subplots()
sc_plot = ax.scatter(x_p, y_p, c=scalar_fields)
ax.set_ylabel('Координата Y, м')
ax.set_xlabel('Координата X, м')
plt.ylim(1200, 0)

cbar = fig.colorbar(sc_plot)
cbar.set_label("Комбинированное скалярное поле")

plt.savefig('cateye.png')