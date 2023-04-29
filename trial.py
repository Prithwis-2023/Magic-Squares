import numpy as np
import math
import itertools
                   
square = np.array([[1,2,98,97,96,5,94,93,9,10], 
                [90,12,13,84,85,86,87,18,19,11],
                [80,79,23,24,76,75,27,28,72,21],
                [70,69,68,34,36,35,37,63,62,31],
                [0,0,0,0,45,46,0,0,0,0],
                [0,0,0,0,55,56,0,0,0,0],
                [40,39,38,64,65,66,67,33,32,61],
                [30,29,73,74,25,26,77,78,22,71],
                [20,82,83,14,16,15,17,88,89,81],
                [91,92,3,7,6,95,4,8,99,100]])    

square_6 = np.array([[1,32,34,3,35,6],
            [30,8,27,28,11,7],
            [0,0,15,16,0,0],
            [0,0,21,22,0,0],
            [12,26,10,9,29,25],
            [31,5,4,33,2,36]])

def square_checker(square):
    sq = list(square)
    l = [] 
    for row in sq:
        l.append(sum(row))
    
    sum_col = 0
    for i in range(int(math.sqrt(sq[-1][-1]))):
        for j in range(int(math.sqrt(sq[-1][-1]))):    
            sum_col = sum_col + sq[j][i]
        l.append(sum_col)    
    
    sum_left = 0
    for j in range(int(math.sqrt(sq[-1][-1]))):
        sum_left = sum_left + sq[j][j]
    l.append(sum_left)    
       
    sum_right = 0
    for k in range(int(math.sqrt(sq[-1][-1]))):
        sum_right = sum_right + sq[k][-(k+1)]
    l.append(sum_right)

    if len(set(l)) == 1:
        print("True")




def solve_algorithm(square):
    dimension = int(math.sqrt(square[-1][-1]))
    sum_square = 0
    for i in range(dimension):
        sum_square = sum_square + square[i][i]
    possible_numerals = [i+1 for i in range(dimension**2)]
    for row in square:
        for number in row:
            if number in possible_numerals:
                possible_numerals.remove(number)
    print(possible_numerals)

l2 = list(square_6[0])[:2] + [2,3] + list(square_6[0])[2:]

square_checker(square_6)

