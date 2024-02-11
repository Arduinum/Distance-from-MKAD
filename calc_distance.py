from math import cos, sin, asin, sqrt, pi


def to_radians(deg:float) -> float:
    """функция для перевода градусов в радианы"""

    return deg * (pi /  180)


def calc_distance(lat1:float, lon1:float, lat2:float, lon2:float) -> float:
    """функция для расчета расстояния между координатами"""

    R =  6371.0  # радиус Земли в километрах

    # преобразование широты и долготы из градусов в радианы
    lat1, lon1, lat2, lon2 = map(to_radians, [lat1, lon1, lat2, lon2])

    # разница между координатами
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # формула гаверсинуса
    a = sin(dlat /  2) **  2 + cos(lat1) * cos(lat2) * sin(dlon /  2) **  2
    c =  2 * asin(sqrt(a))

    # дистанция в километрах
    distance = R * c
    return distance


if __name__ == '__main__':
    # пример использования функции
    lat1, lon1 =  56.330753, 44.006510  # координаты Нижнего Новгорода
    lat2, lon2 =  55.755864, 37.617698  # координаты Москвы
    distance = calc_distance(lat1, lon1, lat2, lon2)
    print(distance, type(distance))
