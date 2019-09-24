import math


def distance(x1, y1, x2, y2):
    distanc = (x2 - x1)**2 + (y2 - y1)**2
    return round(math.sqrt(distanc), 2)
