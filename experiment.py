import math
import sys


def effRec(n):
    pass

def effBF(n):
    pass

def bruteForce(point_set):
    num_points = len(point_set)

    shortest_distance = sys.maxsize - 1
    point1 = None
    point2 = None

    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            distance = math.sqrt(
                    (point_set[i][0] - point_set[j][0]) ** 2
                    + (point_set[i][1] - point_set[j][1]) ** 2)

            if distance < shortest_distance:
                shortest_distance = distance
                point1 = point_set[i]
                point2 = point_set[j]
