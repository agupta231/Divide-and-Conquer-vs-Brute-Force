# Ankur Gupta
# agupta4@wpi.edu
# CS2223 Project 2

import time
import math
import sys


def effRec(n):
    pass

def effBF(n):
    pass

def brute_force(point_set):
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

    return shortest_distance

""" TODO: Make a point sorting function """

def efficient_closest_pair(p, q):
    if len(p) <= 3:
        return brute_force(p)

    else:
        pl = p[:int(len(p)/2)]
        ql = q[:int(len(q)/2)]
        pr = p[int(len(p)/2):]
        qr = p[int(len(q)/2):]

        dl = efficient_closest_pair(pl, ql)
        dr = efficient_closest_pair(pr, qr)
        
        d = min(dl, dr)
        m = p[int(len(p)/2) - 1][0]

        s = []
        for point in q:
            if abs(point[0] - m < d):
                s.append(point)

        dminsq = d ** 2

        for i in range(len(s) - 1):
            k = i + 1

            while k <= len(s) and (s[k][1] - s[i][1]) ** 2 < dminsq:
                dminsq = min((s[k][0] - s[i][0]) ** 2
                        + (s[k][1] - s[i][1]) ** 2,
                        dminsq)
                k += 1

        return math.sqrt(dminsq)

a = [(0, 0),
     (0.5, 26),
     (1, 27),
     (4, 30),
     (10, 100)]

print(brute_force(a))
print(efficient_closest_pair(a, a))
