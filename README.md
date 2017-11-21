# Project 2 - Comparing Divide and Conquer with Brute Force Algorithms

## Ankur Gupta
## CS2223

This program is fairly simple to run. There are 7 functions within the entire program:

* effRec(n) - this function takes in an array of points, will sort it, and then time how long
              it takes for the recursive function (efficient_closest_pair) to compute the 
			  distance between the 2 closest points. The function will then output the 
			  distance as well as how long it took to compute the value.

* effBF(n) - this function takes in an array of points (not required to be sorted), and will
			 time how long it takes for the brute force function to compute the distance between
			 the 2 closest points. The function will then output the distance as well as how
			 long it took to compute the value.

* brute_force(point_set) - this is the function to run the brute force method of finding the 
						   minimal distance between the 2 points. All you need to input
						   is an array of points (doesn't have to be sorted) and the function
						   will return the minimal distance between the 2 closest points.

* efficient_closest_par(p, q) - this is the function to run the recursive  method of finding the 
						        minimal distance between the 2 points. You need to input 2 lists:
								p is the array of points that are sorted with respect to the x 
							    coordinate, and q is the arry of points that are sorted with respect
								to the y cooridinate. The function will return the minimal distance 
								between the 2 closest points.  

* read_input(filename) - this is the parser for the input files that the TA's will test this program
						 on. Assuming that the file is in the same directory as the source code,
						 all that one has to do is input the name of the file, and the function
						 will output the array that is stored in the file.

* sortX(arr) - simple helper function that will return the `arr` sorted in non-decreasing order
			   with respect to the X variable.

* sortY(arr) - simple helper function that will return the `arr` sorted in non-decreasing order
			   with respect to the Y variable.

By default, the program runs the effRec and effBF functions on "input.txt". However, commented out
in the bottom of the code are the three test cases that I made for the program as well:

* required_test - required by the project assignment

* custom_test1 - simple test that is 3 elements long... the brute force and the efficient algorithm
				 should take about the same time, as they are both calling the same function.
				 This point set is custom_test1 = [(1,2), (2,42), (1.3,23)].

* custom_test2 - 0 test. Tests a bunch of elements who count is over 2, and tests the edge case of 
				 a distance of 0 between the 2 closest points. This point set is custom_test2 =
				  [(0,0), (1,5), (123,23), (2, 50), (34,2), (493,23), (2,50), (12,49), (340,230)]


* custom_test3 - large number test. Runs the program on a large set of numbers to see the (near) 
				 asymptotic behavoir of the program. It is here that the recursive program 
				 really begins to shine. This point set is 
				 custom_test3 = [(i / 2, i ** 2) for i in range(10000)]
