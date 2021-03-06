import numpy as np
# Расчитывать будем в Гауссовой системе,так удобнее и нагляднее.
# Скорость света в вакууме
c = 30000000000
# Ток должен быть достаточно большим(в единицах СГСЭ)
I = 3000000000000
const = I/c


def bfield(xrange, yrange, m, coordinates):
    b = np.zeros((xrange, yrange))
    # Определяем длины каждого участка ломаной
    wirelength = coordinates[:, 1:] - coordinates[:, :-1]
    # Делим на мелкие элементы
    divider = np.arange(0, 1, m)
    w1 = np.outer(wirelength[0], divider).T + coordinates[0][:-1]
    w2 = np.outer(wirelength[1], divider).T + coordinates[1][:-1]
    # Длины элементов
    dlx = w1[1] - w1[0]
    dly = w2[1] - w2[0]
    # Координаты центров элементов
    w1 = w1 + dlx / 2
    w2 = w2 + dly / 2
    # Растояния от кусочков до данной точки
    for x in np.arange(xrange):
        for y in np.arange(yrange):
            rx = x - w1
            ry = y - w2
            r = (rx**2 + ry**2)**0.5
            # Собственно говоря, применяем формулу Био-Савара-Лапласа.
            b[x][y] = const*np.abs(np.sum((dlx*ry-dly*rx)/r**3))
    return b.T
