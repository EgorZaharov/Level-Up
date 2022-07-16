import matplotlib.pyplot as plt
import function_for_task_1

a, b, c, discriminant, x1, x2 = 0, 0, 0, 0, 0, 0
x1,x2, discriminant, a, b, c = function_for_task_1.search_values(x1, x2, discriminant, a, b, c)

x_coords = [x for x in range(-10, 10, 1)]

def plotting(x, a, b, c):
    return (a * x ** 2) + (b * x) + c

y_coords = []
for x in x_coords:
    y_coords.append(plotting(x, a, b, c))

plt.plot(x_coords, y_coords )
plt.show()