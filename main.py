from pylab import *
# Расчитывать будем в Гауссовой системе,так удобнее и нагляднее.
# Скорость света в вакууме
c = 30000000000
# Ток должен быть достаточно большим(в единицах СГСЭ)
I = 3000000000000
const = I/c
# Задаем положение проводника
coordinates = []
coord = []
print('Вводится количетсво звеньев ломаной n, затем n строк с последовательными координатами (например,'
      ' n=5;10 10; 20,10; 20,20; 10,20; 10,25)')
for i in range(int(input())):
    s = input().split()
    coordinates.append((int(s[0]), int(s[1])))
print('Magnetic field is being calculated(about 1 minute to wait)...')
# "Делим" проводник на кусочки, которые в дальнейшем будут удобны в подсчёте.
n = 0
for i in range(len(coordinates)-1):
    lx = coordinates[i+1][0] - coordinates[i][0]
    ly = coordinates[i+1][1] - coordinates[i][1]
    l = sqrt(lx**2 + ly**2)
    for j in range(int(l)):
        coord.append((coordinates[i][0]+lx/l*j, coordinates[i][1]+ly/l*j))
        n += 1
    if int(l) != l:
        coord.append((coordinates[i+1][0], coordinates[i+1][1]))


# Расчитываем магнитное поле в произвольной точке пространства
def bfield(x, y, z):
    b0 = 0
    b1 = 0
    b2 = 0
    absb = 0
    for i in range(n-1):
        dlx = coord[i+1][0]-coord[i][0]
        dly = coord[i+1][1]-coord[i][1]
        dlz = 0
        dl = np.array([dlx, dly, dlz])
        # Растояния от кусочка до данной точки
        rx = x - (coord[i][0]+dlx)
        ry = y - (coord[i][1]+dly)
        rz = z
        r = np.array([rx, ry, rz])
        absr = sqrt(rx**2 + ry**2 + rz**2)
        # Собственно говоря, применяем формулу Био-Савара-Лапласа.
        # Используем уже реализованную в numpy функцию векторного произведения(если можно).
        if absr != 0:
            b = const * np.cross(dl, r) / (absr**3)
            # Компоненты вектора магнитной индукции в точке
            b0 += b[0]
            b1 += b[1]
            b2 += b[2]
            # Модуль вектора магнитной индукции, нужен для построения карты силовых линий
            absb += (b[0]**2 + b[1]**2 + b[2]**2)**0.5
    return np.array([b0, b1, b2, absb])


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
            bf = bfield(i, j, k)
            x.append(bf[0]-i)
            y.append(bf[1]-j)
            z.append(bf[2]-k)
            if k==1:
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

