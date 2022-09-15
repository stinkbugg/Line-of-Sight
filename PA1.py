import math
import numpy as np
import argparse

count = 0

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str, help='File containing terrain')

    parser.add_argument('h', type=float, help='h value')

    parser.add_argument('theta', type=float, help='Angle of elevation for Sun')
    parser.add_argument('algorithm', type=str, help='naive | early | fast')
    return parser.parse_args()


def compare(x, y):
    global count
    count += 1
    if abs(x - y) < .000000000001:
        return False
    if x < y:
        return True
    else:
        return False


def print_shade(boolean_array):
    for row in boolean_array:
        for column in row:
            if column == True:
                print ('*    ', end = '')
            elif column == False:
                print ('0    ', end = '')
        print('\n')


def read2Dfloat(fileName):  # read CSV of floats into 2D array
    array2D = []
    # Read input file
    f = open(fileName, "r")
    data = f.read().split('\n')

    # Get 2-D array
    for row in data[0:-1]:
        float_list = list(map(float, row.split(',')[0:-1]))
        array2D.append(float_list)

    return array2D


def runTest(args, terrain=None):
    # Initialize counter
    global count
    count = 0

    theta = np.deg2rad(args.theta)

    if terrain == None:
        terrain = read2Dfloat(args.input_file)

    N = len(terrain)
    shade = [[False] * N for i in range(N)]

    if args.algorithm == 'naive':
        result = naive(terrain, args.h, theta, N, shade)
    elif args.algorithm == 'early':
        result = earlyexit(terrain, args.h, theta, N, shade)
    elif args.algorithm == 'fast':
        result = fast(terrain, args.h, theta, N, shade)

    return result



def naive(image, h, angle, N, shade):
    calcAngle = math.tan(angle)

    for row in range(N):
        for k in range(1, N):
            for j in range(k):
                denom = h * (j - k)
                num = image[row][k] - image[row][j]
                final = num/denom

               #print (compare(final, calcAngle))
                if (compare(calcAngle, final)):
                  shade[row][k] = True

    return shade


def earlyexit(image, h, angle, N, shade):
    calcAngle = math.tan(angle)

    for row in range(N):
        for k in range(1, N):
            for j in range(k):
                denom = h * (j - k)
                num = image[row][k] - image[row][j]
                final = num / denom

                # print (compare(final, calcAngle))
                if (compare(calcAngle, final)):
                    shade[row][k] = True
                    break

    return shade


def fast(image, h, angle, N, shade):
    calcAngle = math.tan(angle)
    myMax = [None] * N

    for row in range(N):
        for k in range(N):
            myMax [k] = image[row][k]

        j=1
        val =0
        max = myMax[0]

        for j in range (N):
            if compare( (myMax[j] + (h * j * calcAngle)), (max + (h * val * calcAngle)) ):
                    shade[row][j] = True

            else:
                max = myMax[j]
                val = j

    return shade


if __name__ == '__main__':
    answer = runTest(getArgs())
    print_shade(answer)
    print('Number of comparisons: ' + str(count))
