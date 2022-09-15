# Line-of-Sight
A python assignment to implement different algorithms for the same problem

# Objective
The objective of PA1 is to implement three different algorithms to solve a line of sight problem. As discussed in lecture, given:\

* image - A 2D N×N array of floating point numbers (in meters) representing a terrain.
* h - The horizontal distance between adjacent points
* angle - The Sun's angle of elevation

The algorithms must return a 2D N×N boolean array where:\
* An entry [i,j] is True if the point [i,j] in the terrain is in the shade
* An entry [i,j] is False if the point [i,j] in the terrain is in the sunlight

The three methods were implemented: naive, early, and fast.
* def naive(image, h, angle, N, shade):

* def earlyexit(image, h, angle, N, shade):

* def fast(image, h, angle, N, shade):

Here, the "shade" parameter represents a 2D N×N boolean array where all values are initialized to False. The code has to update this boolean array and return it. In the implementation, do not use any relations (<,>,<=, or >=) or the functions min()/max(). Anytime a comparison is needed, you are required to use the "compare" method that is provided in the code.

def compare(x,y):
 
This boolean function expects two floats x and y. It returns a value of True if x is less than y. It returns False otherwise.

# Running the code
The program requires 4 command-line arguments to run.

python3 PA1.py [file_name] [h] [theta] [algorithm]  

* file_name - name of input file containing a square terrain (2D array)
* h - horizontal distance between adjacent points
* theta - Sun's angle of elevation
* algorithm - a string containing the name of the method to run (naive|early|fast)

# Example 

python3 PA1.py elev15x15.txt 1 45 naive

This will run with the terrain elev15x15.txt with the naive method, h=1 and theta=45

0    0    *    *    *    *    *    *    *    0    *    *    *    *    *    

0    0    *    0    0    *    *    *    *    *    *    *    *    *    *    

0    *    *    0    0    *    *    *    *    *    0    *    *    *    *    

0    0    *    *    *    *    0    *    *    *    0    *    *    *    *    

0    *    *    0    *    *    *    *    *    *    0    *    0    *    *    

0    *    0    *    *    *    0    *    0    *    *    *    *    *    *    

0    *    *    *    0    *    *    0    *    *    *    *    0    *    0    

0    0    0    *    *    0    0    *    0    0    *    *    *    *    *    

0    *    *    *    *    *    *    *    0    *    *    *    *    *    0    

0    0    *    *    *    *    *    *    *    *    *    *    *    0    *    

0    *    *    *    *    0    *    *    *    *    *    *    *    *    0    

0    0    *    *    *    *    *    0    0    *    *    *    *    *    *    

0    *    *    0    *    0    *    *    0    *    *    0    0    *    *    

0    0    *    *    *    *    *    *    *    *    0    *    *    0    *    

0    0    0    0    0    *    *    0    0    *    *    0    *    *    *    

Number of comparisons: 1575

