#2次元set
def uniq2d(A):
    B = list(map(list, set(map(tuple, A))))
    return B
