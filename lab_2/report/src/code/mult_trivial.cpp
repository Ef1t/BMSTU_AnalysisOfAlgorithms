def default_mult(matrix1, matrix2):
    if get_columns(matrix1) != get_rows(matrix2):
        print('Error')
        return

    result = [[0 for j in range(get_rows(matrix1))] 
        for i in range(get_columns(matrix2))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result