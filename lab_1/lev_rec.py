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