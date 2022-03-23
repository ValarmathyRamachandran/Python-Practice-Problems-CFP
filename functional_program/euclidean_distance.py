import math


def distance(x, y):
    p1 = [0, 0]
    p2 = [x, y]
    euclidean_distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    print(euclidean_distance)


distance(6, 6)
