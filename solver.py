import numpy as np
# Расчитывать будем в Гауссовой системе,так удобнее и нагляднее.
# Скорость света в вакууме
c = 30000000000
# Ток должен быть достаточно большим(в единицах СГСЭ)
I = 3000000000000
const = I/c


def divide(coordinates):
    coord = []
    for i in range(len(coordinates) - 1):
        lx = coordinates[i + 1][0] - coordinates[i][0]
        ly = coordinates[i + 1][1] - coordinates[i][1]
        l = (lx ** 2 + ly ** 2)**0.5
        for j in range(int(l)):
            coord.append((coordinates[i][0] + lx / l * j, coordinates[i][1] + ly / l * j))
        if int(l) != l:
            coord.append((coordinates[i + 1][0], coordinates[i + 1][1]))
    return coord


def bfield(x, y, z, coord):
    b0 = 0
    b1 = 0
    b2 = 0
    absb = 0
    for i in range(len(coord)-1):
        dlx = coord[i+1][0]-coord[i][0]
        dly = coord[i+1][1]-coord[i][1]
        dlz = 0
        dl = np.array([dlx, dly, dlz])
        # Растояния от кусочка до данной точки
        rx = x - (coord[i][0]+dlx)
        ry = y - (coord[i][1]+dly)
        rz = z
        r = np.array([rx, ry, rz])
        absr = (rx**2 + ry**2 + rz**2)**0.5
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
