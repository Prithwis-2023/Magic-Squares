import numpy as np
import math
import itertools

#checking for commonality
def common(a,b):
    out = any(check in a for check in b)
    if out:
        return True
    else:
        return False

#checking if the square is indeed a magic square
def is_magic_square(square):
    # Calculate the expected sum of each row, column, and diagonal
    n = len(square)
    expected_sum = n * (n**2 + 1) // 2
    
    # Check rows and columns
    for i in range(n):
        row_sum = sum(square[i])
        col_sum = sum(square[j][i] for j in range(n))
        if row_sum != expected_sum or col_sum != expected_sum:
            return False 
    
    # Check diagonals
    diagonal_sum1 = sum(square[i][i] for i in range(n))
    diagonal_sum2 = sum(square[i][n-1-i] for i in range(n))
    if diagonal_sum1 != expected_sum or diagonal_sum2 != expected_sum:
        return False
    
    # If all checks passed, it is a magic square
    return True

#designed as per my research of construction
def generator(n):   #n is the desired dimension
    matrix = np.zeros((n,n), dtype=int)
    matrix[0][0] = 1
    matrix[0][n-1] = n
    matrix[n-1][n-1] = n**2
    matrix[n-1][0] = n**2 - n + 1
    matrix[1][0] = n*(n-1) 
    matrix[1][n-1] = matrix[0][n-1] + 1
    matrix[n-2][0] = 2*n
    matrix[n-2][-1] = (n-1)**2

    commondiff0 = (matrix[n-1][n-1] - matrix[0][0]) / (n - 1)
    commondiff1 = (matrix[n-1][0] - matrix[0][n-1]) / (n - 1)
    for i in range(1,n-1):
        matrix[i][i] = matrix[i-1][i-1] + commondiff0
        matrix[i][-(i+1)] = matrix[i-1][-i] + commondiff1

    blanks = int((n-10) / 4) + 2            #to be left in the first and last rows
    for i in range(1, blanks):
        matrix[0][i] = matrix[0][i-1] + 1
        matrix[n-1][i] = matrix[n-1][i-1] + 1    
    for i in range(2, blanks + 1):
        matrix[0][-i] = matrix[0][-i+1] - 1
        matrix[n-1][-i] = matrix[n-1][-i+1] - 1

    matrix[0][int(n / 2)] = int(n / 2)
    matrix[n-1][int(n / 2)] = n**2 - int(n / 2)
    matrix[n-1][int(n / 2) - 1] = int(n / 2) + 1
    matrix[0][int(n / 2) - 1] = matrix[n-1][int(n / 2)] + 1
    
    for i in range(int(n / 2) - 2, blanks-1, -1):
            matrix[0][i] = matrix[0][i+1] + 1 
    for i in range(int(n / 2) - 1 , n - blanks - 1):
        matrix[0][i+1] = matrix[0][i] - 1 
    matrix[0][int(n / 2)] = int(n / 2)        #changing the value back to n/2    

    matrix[n-1][int(n / 2) + 1] = matrix[0][int(n / 2)] - 1
    matrix[n-1][int(n / 2) - 2] = matrix[n-1][int(n / 2) - 1] + 1

    for i in range(0, (int(n / 2) - 2)):
        matrix[n-1][i] = 1 + i
    matrix[n-1][0] = matrix[0][n-1] + (n - 1) * commondiff1
    for i in range(1, blanks):    
        matrix[n-1][i] = matrix[n-1][i-1] + 1 

    matrix[n-1][(-1 * blanks) - 1] = matrix[0][-1 * blanks] - 1   #for the zeros that are still left in the last row
    for i in (-blanks-1, -(int(n / 2) + 1)):
        matrix[n-1][i-1] = matrix[n-1][i] - 1
        #pass

    for i in range(1, int((n - 10) / 4) + 3):
        for j in range(i, i + blanks-1):
           matrix[i][j+1] = matrix[i][j] + 1
           matrix[n-i-1][j+1] = matrix[n-i-1][j] + 1 
        for j in (-i - 1, -i - blanks + 1):
            matrix[i][j-1] = matrix[i][j] - 1
            matrix[n-i-1][j-1] = matrix[n-i-1][j] - 1
    return matrix    

#tailored for solving the two middle rows of the particular class of magic squares being generated
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
        for p in range(len(combs1)):
            if common(list(combs0[l]), list(combs1[p])) == False:
                if square[half][half-1] not in list(combs0[l]) and square[half][half] not in list(combs0[l]) and square[half-1][half-1] not in list(combs1[p]) and square[half-1][half] not in list(combs1[p]):
                    perm0 = list(itertools.permutations(list(combs0[l]), dimension-2))
                    perm1 = list(itertools.permutations(list(combs1[p]), dimension-2))
                    
                    for j in range(len(perm0)):
                        for q in range(len(perm1)):
                            #perm0[j] = list(perm0[j])
                            #perm1[q] = list(perm1[q])
                            if common(list(perm0[j]), list(perm1[q])) == False:
                                perm0_mod = list(perm0[j])[:(half-1)] + [square[half-1][half-1], square[half-1][half]] + list(perm0[j])[(half-1):]
                                #list(perm0[j]).insert(square[half-1][half-1], half-1)
                                #list(perm0[j]).insert(square[half-1][half], half)
                                perm1_mod = list(perm1[q])[:(half-1)] + [square[half][half-1], square[half][half]] + list(perm1[q])[(half-1):]
                                #list(perm1[q]).insert(square[half][half-1], half-1)
                                #list(perm1[q]).insert(square[half][half], half)
                                
                                mod_sq= []
                                for k in range(half-1):
                                    mod_sq.append(list(square[k]))
                                mod_sq.append(perm0_mod)
                                mod_sq.append(perm1_mod)    
                                for k in range((half+1),dimension):
                                    mod_sq.append(list(square[k]))
                                
                                magic = np.array(mod_sq)    
                                if is_magic_square(magic) == True:
                                    print(magic)
                                    print("-----------------------------------------------")
  