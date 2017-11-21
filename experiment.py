# Ankur Gupta
# agupta4@wpi.edu
# CS2223 Project 2

# Imports
import time
import math
import sys


# Timer function for the recursive method
def effRec(n):
    p = sortX(n)
    q = sortY(n)

    start_time = time.clock()
    distance = efficient_closest_pair(p, q)
    end_time = time.clock()
    
    print("Efficient Algorithm Distance: " + str(distance) + " Time: " + str(end_time - start_time))


# Timer function for the brute force method
def effBF(n):
    start_time = time.clock()
    distance = brute_force(n)
    end_time = time.clock()
    
    print("Brute Force Distance: " + str(distance) + " Time: " + str(end_time - start_time))


# Brute force function. Takes in a list and compares each value until a shortest distance
#     is found
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


# Recursive function. Takes in 2 lists: one with the points sorted with respect to x
#     and one with the points sorted with respect to y
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

            while k < len(s) and (s[k][1] - s[i][1]) ** 2 < dminsq:
                dminsq = min((s[k][0] - s[i][0]) ** 2
                        + (s[k][1] - s[i][1]) ** 2,
                        dminsq)
                k += 1

        return math.sqrt(dminsq)


# Parser for the input file that will be given by the grader
def read_input(filename):
    points_array = []

    with open(filename) as file_pointer:
        points_array = []

        for line in file_pointer:
            for i in range(len(line)):
                if line[i] == "(":
                    flag_first_point = True
                    flag_second_point = False
                    first_point = ""
                    second_point = ""

                    for j in range(i + 1, len(line)):
                        if line[j] == ",":
                            flag_first_point = False
                            flag_second_point = True
                        elif line[j] == ")":
                            i = j
                            break
                        elif flag_first_point:
                            first_point += line[j]
                        elif flag_second_point:
                            second_point += line[j]

                    points_array.append((int(first_point), int(second_point)))
    
    return points_array


# Returns the array sorted with respect to the x coordinate
def sortX(arr):
    return sorted(arr, key=lambda x: x[0])


# Returns the array sorted with respect to the y coordinate
def sortY(arr):
    return sorted(arr, key=lambda x: x[1])

required_test = [(0,0),
                 (7,6),
                 (2,20),
                 (12,5),
                 (16,16),
                 (5,8),
                 (19,7),
                 (14,22),
                 (8,19),
                 (7,29),
                 (10,11),
                 (1,13)]

custom_test1 = [(1,2),
         (2,42),
         (1.3,23)]


custom_test2 = [(0,0),
         (1,5),
         (123,23),
         (2, 50),
         (34,2),
         (493,23),
         (2,50),
         (12,49),
         (340,230)]

custom_test3 = [(i / 2, i ** 2) for i in range(10000)] 




input_array = read_input("input.txt")

print("input.txt")
effBF(input_array)
effRec(input_array)

print("required_test")
effBF(required_test)
effRec(required_test)

print("test1")
effBF(custom_test1)
effRec(custom_test1)

print("test2")
effBF(custom_test2)
effRec(custom_test2)

print("test3")
effBF(custom_test3)
effRec(custom_test3)
