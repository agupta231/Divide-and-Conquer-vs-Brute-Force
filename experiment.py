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

""" TODO: Make a point sorting function """

def efficient_closest_pair(p, q):
    if len(p) <= 3:
        brute_force(p)
    else:
        pl = p[:int(len(p)/2)]
        ql = q[:int(len(q)/2)]
        pr = p[int(len(p)/2):]
        qr = p[int(len(q)/2):]

        dl = efficient_closest_pair(pl, ql)
        dr = efficient_closest_pair(pr, qr)
        
        min_distance = min(dl, dr)
