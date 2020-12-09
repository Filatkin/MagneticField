import matplotlib.pyplot as plt
from solver import *
# Задаем положение проводника
coordinates = []

print('Вводится количетсво звеньев ломаной n, затем n строк с последовательными координатами (например,'
      ' n=5;10 10; 20,10; 20,20; 10,20; 10,25)')

for i in range(int(input())):
    s = input().split()
    coordinates.append((int(s[0]), int(s[1])))

coordinates = np.array(coordinates).T

print('Magnetic field is being calculated...')
# Задаём объём простарнства, в каждой точке которого будет посчитана индукция.
x = 30
y = 30
bmatrix = np.zeros((x, y))
# Непосредственно подсчёт
for i in range(x):
    for j in range(y):
        bmatrix[i][j] = bfield(i, j, coordinates)
# Рисуем, что получилось
fig, ax = plt.subplots()
x = range(x)
y = range(y)
z = bmatrix.T
# Линиями уровня функции B=B(x1,y1) удобно построить карту силовых линий(из физики известно, что силовые линии
# магнитного поля представляются как изолинии магнитного потока).
ax.contour(x, y, z, 35)
plt.title('Карта силовых линий магнитного поля (видны также искажения вследствие краевых эффектов)')
plt.show()

