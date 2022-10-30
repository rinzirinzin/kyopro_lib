import bisect
import collections
import copy
import heapq
import itertools
import math
import sys
from collections import deque
from itertools import groupby, product

#累積和
def ruiseki(A):
    S = list(itertools.accumulate(A))
    return S

#2次元累積和 (多分もう少し早い方法ある)
def ruiseki_2d(X,H,W):
    Sx = []
    for i in range(H):
        Sx.append(ruiseki(X[i]))
    Sy = [[0]*H for _ in range(W)]
    for i in range(H):
        for j in range(W):
            Sy[j][i] = Sx[i][j]
    S = []
    for i in range(W):
        S.append(ruiseki(Sy[i]))
    S2d = [[0]*W for i in range(H)]
    for i in range(H):
        for j in range(W):
            S2d[i][j] = S[j][i]
    return S2d
