def matrix_test():
    M = random.randint(1, 30)
    N = random.randint(1, 30)
    Q = random.randint(1, 30)

    matrix1 = [[random.randint(1, 100) for j in range(M)] 
    			for i in range(N)]
    matrix2 = [[random.randint(1, 100) 
    			for j in range(N)] for i in range(Q)]

    res1 = default_mult(matrix1, matrix2)
    res2 = winograd_multiply(matrix1, matrix2)
    res3 = improved_winograd_multiply(matrix1, matrix2)

    return res1 == res2 == res3

    