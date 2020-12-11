from time import *
import random
import string
import sys


# Other functions
def takeRandomString(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


def tablePrint(matrix):
    print("\n Result matrix:")

    for row in matrix:
        for element in row:
            print("{:4d}".format(element), end="")
        print()



# Algorithms
def lev_rec(s1, s2):
    if (s1 == "" or s2 == ""):
        return len(s1) + len(s2)
    temp = 0 
    if (s1[-1] != s2[-1]): 
        temp = 1
    return min(lev_rec(s1[:-1], s2) + 1, lev_rec(s1, s2[:-1]) + 1, lev_rec(s1[:-1], s2[:-1]) + temp)
    

def lev_matrix(s1, s2, isPrint):
    n = len(s1) + 1
    m = len(s2) + 1
    matrix = []
    for i in range(n):
        temp_matrix = []
        matrix.append(temp_matrix)
        for j in range(m):
            temp_matrix.append(i + j)

    for i in range(1, n):
        for j in range(1, m):
            temp = 0 
            if (s1[i - 1] != s2[j - 1]):
                temp = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + temp)

    if (isPrint):
        tablePrint(matrix)
    
    return matrix[-1][-1]


def lev_matrix_rec(matrix, row, column, s1, s2):
    if row == 0: 
        return column 
    if column == 0: 
        return row 
    if matrix[row][column] == -1: 
        matrix[row][column] = min(lev_matrix_rec(matrix, row, column - 1, s1, s2) + 1, 
        lev_matrix_rec(matrix, row - 1, column, s1, s2) + 1, 
        lev_matrix_rec(matrix, row - 1, column - 1, s1, s2) + int(s1[row - 1] != s2[column - 1])) 
    return matrix[row][column]
    # if (i + 1 < len(table)) and (j + 1 < len(table[0])):
    #     temp = 0
    #     if s1[j] != s2[i]:
    #         temp = 1 
    #     if table[i + 1][j + 1] > table[i][j] + temp:
    #         table[i + 1][j + 1] = table[i][j] + temp
    #         lev_matrix_rec(table, i + 1, j + 1, s1, s2)
    
    # if (j + 1 < len(table[0])) and (table[i][j + 1] > table[i][j] + 1):
    #     table[i][j + 1] = table[i][j] + 1
    #     lev_matrix_rec(table, i, j + 1, s1, s2)

    # if (i + 1 < len(table)) and (table[i + 1][j] > table[i][j] + 1):
    #     table[i + 1][j] = table[i][j] + 1
    #     lev_matrix_rec(table, i + 1, j, s1, s2)
            
            
def lev_matrixRecursion(s1, s2, isPrint):
    # lenI = len(s1) + 1
    # lenJ = len(s2) + 1

    # maxLen = max(len(s1), len(s2)) + 1

    # table = [[maxLen] * lenI for i in range(lenJ)]
    # table[0][0] = 0

    
    # tablePrint(table)

    # lev_matrix_rec(table, 0, 0, s1, s2)
    matrix = [[-1 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)] 
    lev_matrix_rec(matrix, len(s1), len(s2), s1, s2) 

    # if isPrint:
    # tablePrint(matrix)
    
    return matrix[-1][-1]


def damerauLevenstein(s1, s2, isPrint):
    n = len(s1) + 1
    m = len(s2) + 1
    matrix = [[i + j for j in range(m)] for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            temp = 0
            if (s1[i - 1] != s2[j - 1]):
                temp = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,matrix[i][j - 1] + 1,matrix[i - 1][j - 1] + temp)
            if (i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]):
                matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + 1)

    if isPrint:
        tablePrint(matrix)
    
    return matrix[-1][-1]



# Unit tests
def doUnitTest(testArray, testName, levFunction, isTable):
    for i in range(len(testArray)):
        if (isTable):
            result = levFunction(testArray[i][0], testArray[i][1], False)
        else:
            result = levFunction(testArray[i][0], testArray[i][1])

        if (result == testArray[i][2]):
            print(testName, "test", i, "succesfully")
        else:
            print(testName, "test", i, "failure")
            return False
    
    return True


def unitTests(levFunction, isTable):
    # Тесты при пустых входных строках
    test_empty = [["f", "f", 0], ["f", "", 1], ["", "f", 1]]
    # Тесты на поиск совпадений
    test_match = [["asd", "asd", 0], ["f", "f", 0], ["F", "f", 1]]
    # Остальные тесты
    test_others = [["a", "s", 1], ["asd", "bsf", 2], ["asd", "as", 1], ["a", "adws", 3]]

    if doUnitTest(test_empty, "Empty", levFunction, isTable):
        print()
        if doUnitTest(test_match, "Match", levFunction, isTable):
            print()
            if doUnitTest(test_others, "Others", levFunction, isTable):
                print("\n All tests done!\n")



# Time tests
def doTimeTestsRecursion(levFunction, iterations, strLength):
    t1 = process_time()

    for _ in range(iterations):
        s1 = takeRandomString(strLength)
        s2 = takeRandomString(strLength)
        levFunction(s1, s2)

    t2 = process_time()

    return (t2 - t1) / iterations


def doTimeTestsTable(levFunction, iterations, strLength):
    t1 = process_time()

    for _ in range(iterations):
        s1 = takeRandomString(strLength)
        s2 = takeRandomString(strLength)
        levFunction(s1, s2, False)

    t2 = process_time()

    return (t2 - t1) / iterations


def timeTests(levFunction, isTable, isRecursion):
    lengthsArray = [1, 3, 7, 20, 100, 1000]
    iterations   = [100000, 100, 100, 200, 100, 10]

    if (isRecursion):
        lastIndex = 3
    else:
        lastIndex = len(lengthsArray)

    for i in range(lastIndex):
        if (isTable):
            timeResult = doTimeTestsTable(levFunction, iterations[i], lengthsArray[i])
        else:
            timeResult = doTimeTestsRecursion(levFunction, iterations[i], lengthsArray[i])
        
        print("For length =", lengthsArray[i], "\ttime =", timeResult)



def main():
    done = False

    while(not done):

        # print("Choose operation: ")
        print("1 - Recursion")
        print("2 - Matrix")
        print("3 - Matrix + Recursion")
        print("4 - Damerau-Levenstein")
        # print("5 - Unit tests")
        print("5 - Time tests")
        print("0 - Exit\n")

        try:
            action = int(input("  Choice: "))
        except:
            print("\n   Wrong operation \n")
            continue

        if (action == 0):
            done = True
            continue
        elif (action != 5 and action != 6):
            word1 = input("  Input first  word: ")
            word2 = input("  Input second word: ")

        if (action == 1):
            result = lev_rec(word1, word2)
        elif (action == 2):
            result = lev_matrix(word1, word2, True)
        elif (action == 3):
            result = lev_matrixRecursion(word1, word2, True)
        elif (action == 4):
            result = damerauLevenstein(word1, word2, True)
        elif(action == 5):
            result = False

            print(" Test for Levenstein recursion:\n")
            unitTests(lev_rec, False)

            print(" Test for Levenstein table:\n")
            unitTests(lev_matrix, True)

            print(" Test for Levenstein recursion-table:\n")
            unitTests(lev_matrixRecursion, True)

            print(" Test for Damerau-Levenstein:\n")
            unitTests(damerauLevenstein, True)
        elif(action == 6):
            print("\n Time test for Levenstein recursion:")
            timeTests(lev_rec, False, True)

            print("\n Time test for Levenstein table:")
            timeTests(lev_matrix, True, False)

            print("\n Time test for Levenstein recursion-table:")
            timeTests(lev_matrixRecursion, True, True)

            print("\n Time test for Damerau-Levenstein:")
            timeTests(damerauLevenstein, True, False)
            
            result = False

        if (result):
            print("\n  Result: ", result, "\n")


main()