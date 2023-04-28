from itertools import combinations

# given list of numbers
numbers = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

# find all combinations of four numbers from the list
combs = list(combinations(numbers, 10))

l0 =  []
# check each combination's sum
for comb in combs:
    if sum(list(comb)) == 505 and numbers[4] in list(comb) and numbers[5] in list(comb) and numbers[-3] in list(comb) and numbers[-8] in list(comb) and numbers[-5] not in list(comb) and numbers[-6] not in list(comb):
            l0.append(list(comb))

