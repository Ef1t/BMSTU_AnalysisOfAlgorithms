def winograd_multiply(matrix1, matrix2):
    if get_columns(matrix1) != get_rows(matrix2):
        print('Error')
        return

    M = get_rows(matrix1)
    N = get_columns(matrix1)
    Q = get_columns(matrix2)
    
    result = [[0 for j in range(M)] 
        for i in range(Q)]

    mulH = [0 for i in range(M)]
    for i in range(M):
        for j in range(int(N / 2)):
            mulH[i] += matrix1[i][j * 2] * matrix1[i][j * 2 + 1]

    mulV = [0 for i in range(Q)]
    for i in range(Q):
        for j in range(int(N / 2)):
            mulV[i] += matrix2[j * 2][i] * matrix2[j * 2 + 1][i]

    for i in range(M):
        for j in range(Q):
            result[i][j] = -mulH[i] - mulV[j]
            for k in range(int(N / 2)):
                result[i][j] += (matrix1[i][2 * k] + 
                    matrix2[2 * k + 1][j]) * (matrix1[i][2 * k + 1] + 
                        matrix2[2 * k][j])

    if N % 2 == 1:
        for i in range(M):
            for j in range(Q):
                result[i][j] += matrix1[i][N - 1] *
                    matrix2[N - 1][j]

    return result