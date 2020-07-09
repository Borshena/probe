import simple_draw as sd
import math


sd.resolution = (1200, 600)
x, y = 600, 300
point = sd.get_point(x, y)
sd.circle(point, 50, sd.COLOR_YELLOW, 0)
x_ray = []
y_ray = []
point_ray = []
q = 0.79
k = 0
for i in range(8):
    x1 = x + 100 * math.cos(k)
    y1 = y + 100 * math.sin(k)
    k += q
    x_ray.append(x1)
    y_ray.append(y1)
    point_ray.append(sd.get_point(x1, y1))

for i in range(8):
    sd.line(point, point_ray[i])
sd.pause()
