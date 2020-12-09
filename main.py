from pylab import *
from solver import *
# Задаем положение проводника
coordinates = []

print('Вводится количетсво звеньев ломаной n, затем n строк с последовательными координатами (например,'
      ' n=5;10 10; 20,10; 20,20; 10,20; 10,25)')

for i in range(int(input())):
    s = input().split()
    coordinates.append((int(s[0]), int(s[1])))

# coordinates = np.array(coordinates).T

print('Magnetic field is being calculated(about 1 minute to wait)...')

# Делим проводник на малые кусочки.
coord = divide(coordinates)

# Задаём объём простарнства, в каждой точке которого будет посчитана индукция.
xwidth = 30
ywidth = 30
zwidth = 30
x = []
y = []
z = []
bmatrix = np.zeros((xwidth, ywidth))
# Непосредственно подсчёт
for i in range(xwidth):
    for j in range(ywidth):
        k = -zwidth/2
        while k != zwidth/2:
            bf = bfield(i, j, k, coord)
            x.append(bf[0]-i)
            y.append(bf[1]-j)
            z.append(bf[2]-k)
            if k == 1:
                bmatrix[i][j] = bf[2]
            k += 1
# Рисуем, что получилось
fig = plt.figure()
ax = fig.add_subplot(212, projection='3d')
ax.plot(x, y, z)
title('Векторное представление линий магнитной индукции')
x1 = range(xwidth)
y1 = range(ywidth)
z1 = bmatrix[x1][y1].T
ax1 = fig.add_subplot(211)
# Линиями уровня функции B=B(x1,y1) удобно построить карту силовых линий.
ax1.contour(x1, y1, z1, 35)
title('Карта силовых линий магнитного поля данного проводника(видны также искажения вследствие краевых эффектов)')
plt.show()

