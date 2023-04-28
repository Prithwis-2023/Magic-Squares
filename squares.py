import numpy as np
import math
import itertools

square_10 = np.array([[1,2,98,97,96,5,94,93,9,10], 
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

def common(a,b):
    out = any(check in a for check in b)
    if out:
        return True
    else:
        return False

def square_checker(square):
    l = [] 
    for row in square:
        l.append(sum(row))
    
    for i in range(int(math.sqrt(square[-1][-1]))):
            l.append(sum(square[:,i]))    
    
    sum_left = 0
    for j in range(int(math.sqrt(square[-1][-1]))):
        sum_left = sum_left + square[j][j]
    l.append(sum_left)    
       
    sum_right = 0
    for k in range(int(math.sqrt(square[-1][-1]))):
        sum_right = sum_right + square[k][-(k+1)]
    l.append(sum_right)

    if len(set(l)) == 1:
        print(square)


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
    
    combs0= list(itertools.combinations(possible_numerals, dimension-2))
    combs1= list(itertools.combinations(possible_numerals, dimension-2))

    half = int(dimension / 2)

    for l in range(len(combs0)):
        if common(list(combs0[l]), list(combs1[l])) == False:
            if square[half][half-1] not in list(combs0[l]) and square[half][half] not in list(combs0[l]) and square[half-1][half-1] not in list(combs1[l]) and square[half-1][half] not in list(combs1[l]):
                perm0 = list(itertools.permutations(list(combs0[l]), dimension-2))
                perm1 = list(itertools.permutations(list(combs1[l]), dimension-2))
                
                for j in range(len(perm0)):
                    perm0[j] = list(perm0[j])
                    perm1[j] = list(perm1[j])
                    if common(perm0[j], perm1[j]) == False:
                        perm0[j].insert(square[half-1][half-1], half-1)
                        perm0[j].insert(square[half-1][half], half)
                        perm1[j].insert(square[half][half-1], half-1)
                        perm1[j].insert(square[half][half], half)
                        
                        mod_sq= []
                        for k in range(half-1):
                            mod_sq.append(square[k])
                        mod_sq.append(perm0[j])
                        mod_sq.append(perm1[j])    
                        for k in range((half+1),dimension):
                            mod_sq.append(square[k])
                        
                        magic = np.array(mod_sq)    
                        #square_checker(magic)
                        print(magic)

solve_algorithm(square_6)    