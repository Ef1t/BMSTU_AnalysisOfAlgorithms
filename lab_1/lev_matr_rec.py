def lev_matrix_rec(matrix, row, column, source, target):
    if row == 0: 
        return column 
    if column == 0: 
        return row 
    if matrix[row][column] == -1: 
        matrix[row][column] = min(lev_matrix_rec(matrix, row, 
            column - 1, source, target) + 1, 
        lev_matrix_rec(matrix, row - 1, column, source, target) + 1, 
        lev_matrix_rec(matrix, row - 1, column - 1, source, target) + 
            int(source[row - 1] != target[column - 1])) 
    
    return matrix[row][column]

def lev_matrix_recursion(source, target):
    matrix = [[-1 for j in range(len(target) + 1)] 
        for i in range(len(source) + 1)] 
    lev_matrix_rec(matrix, len(source), len(target), source, target) 

    return matrix[-1][-1]