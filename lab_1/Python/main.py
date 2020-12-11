from math import inf
import random
from time import time
import string

def random_string(str_len):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(str_len))

def lev_rec(source, target):
    if len(source) == 0 or len(target) == 0:
        return abs(len(source) - len(target))
    
    if (source[-1] == target[-1]):
        additional = 0
    else: 
        additional = 1

    return min(lev_rec(source, target[:-1]) + 1,
               lev_rec(source[:-1], target) + 1,
               lev_rec(source[:-1], target[:-1]) + additional)

def lev_matrix(source, target):
    data = [[i + j for j in range(len(target) + 1)] for i in range(len(source) + 1)]
    
    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if (source[i - 1] == target[j - 1]):
                additional = 0
            else:
                additional = 1
           
            data[i][j] = min(data[i - 1][j] + 1, data[i][j - 1] + 1, data[i - 1][j - 1] + additional)

    return data[-1][-1]

def lev_matrix_rec(matrix, row, column, source, target):
    if row == 0: 
        return column 
    if column == 0: 
        return row 
    if matrix[row][column] == -1: 
        matrix[row][column] = min(lev_matrix_rec(matrix, row, column - 1, source, target) + 1, 
        lev_matrix_rec(matrix, row - 1, column, source, target) + 1, 
        lev_matrix_rec(matrix, row - 1, column - 1, source, target) + int(source[row - 1] != target[column - 1])) 
    return matrix[row][column]

def lev_matrix_recursion(source, target):
    matrix = [[-1 for j in range(len(target) + 1)] for i in range(len(source) + 1)] 
    lev_matrix_rec(matrix, len(source), len(target), source, target) 

    return matrix[-1][-1]

def damer_lev(source, target):
    data = [[i + j for j in range(len(target) + 1)] for i in range(len(source) + 1)]
    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if source[i - 1] == target[j - 1]:
                additional = 0
            else:
                additional = 1
            data[i][j] = min(data[i - 1][j] + 1, data[i][j - 1] + 1, data[i - 1][j - 1] + additional)

            if (i > 1 and j > 1 and source[i - 1] == target[i - 2] and source[i - 2] == target[i - 1]):
                data[i][j] = min(data[i][j], data[i - 2][j - 2] + 1)

    return data[-1][-1]

def process(function):
    source = input("Input source: ")
    target = input("Input target: ")
    res = function(source, target)
    print("Distance = ", res)


def time_analysis(function, n_iter, str_len):
    t1 = time()
    for i in range(n_iter):
        source = random_string(str_len)
        target = random_string(str_len)
        function(source, target)
    t2 = time()
    return (t2 - t1) / n_iter


def menu():
    run = True
    while (run):
        case = input("Menu:\n \
    1. Levenshtein distance recursion\n \
    2. Levenshtein distance matrix\n \
    3. Levenshtein distance matrix recursion\n \
    4. Damerau–Levenshtein distance matrix\n \
    5. All in one\n \
    6. Time analysis\n ")
        if (case == "1"):
            process(lev_rec)
        elif (case == "2"):
            process(lev_matrix)
        elif (case == "3"):
            process(lev_matrix_rec)
        elif (case == "4"):
            process(damer_lev)
        elif (case == "6"):
            n_iter = 100
            for i in range(1, 10):
                print("Strlen: ", i)
                print("Lev recursion   : ", "{0:.15f}".format(time_analysis(lev_rec, n_iter, i)))
                print("Lev matrix       : ", "{0:.15f}".format(time_analysis(lev_matrix, n_iter, i)))
                print("Lev matrix recursion: ", "{0:.15f}".format(time_analysis(lev_matrix_recursion, n_iter, i)))
                print("Dam-Lev matrix     : ", "{0:.15f}".format(time_analysis(damer_lev, n_iter, i)))
        elif (case == "5"):
            output = True
            source = input("Input source: ")
            target = input("Input target: ")
            print("Distance Lev rec = ", lev_rec(source, target))
            print("Distance Lev matr = ", lev_matrix(source, target))
            print("Distance Lev matr rec = ", lev_matrix_rec(source, target))
            print("Distance Damer-Lev = ", damer_lev(source, target))
            
        else:
            run = False
            
            
if __name__ == "__main__": 
	menu()
    