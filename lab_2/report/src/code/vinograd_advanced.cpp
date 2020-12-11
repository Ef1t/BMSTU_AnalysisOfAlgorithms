def improved_winograd_multiply(matrix1, matrix2):
    if get_columns(matrix1) != L:
        print('Error')
        return

    M = get_rows(matrix1)
    N = get_columns(matrix1)
    Q = get_columns(matrix2)
    L = get_rows(matrix2)
    Lmod2 = L % 2
    Nmod2 = N % 2

    result = [[0 for j in range(M)] 
        for i in range(Q)]

    mulH = [0 for i in range(M)]
    mulV = [0 for i in range(Q)]

    for i in range(M):
        for j in range(0, N - Nmod2, 2):
            mulH[i] += matrix1[i][j] * matrix1[i][j + 1]

    for i in range(Q):
        for j in range(0, L - Lmod2, 2):
            mulV[i] += matrix2[j][i] * matrix2[j + 1][i]

    for i in range(M):
        for j in range(Q):
            buff = -mulH[i] - mulV[j]
            for k in range(0, N - 
                Nmod2, 2):
                buff += (matrix1[i][k + 1] + matrix2[k][j]) * 
                        (matrix1[i][k] + matrix2[k + 1][j])
            result[i][j] = buff

    if Nmod2:
        for i in range(M):
            for j in range(Q):
                result[i][j] += matrix1[i][N - 1] * 
                    matrix2[N - 1][j]

    return result