def damer_lev(source, target):
    data = [[i + j for j in range(len(target) + 1)] 
            for i in range(len(source) + 1)]

    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if source[i - 1] == target[j - 1]:
                additional = 0
            else:
                additional = 1
            data[i][j] = min(data[i - 1][j] + 1, 
                data[i][j - 1] + 1, 
                data[i - 1][j - 1] + additional)

            if (i > 1 and j > 1 and 
                source[i - 1] == target[i - 2] and 
                source[i - 2] == target[i - 1]):
                data[i][j] = min(data[i][j], data[i - 2][j - 2] + 1)

    return data[-1][-1]