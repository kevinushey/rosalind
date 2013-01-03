import os
import sys

sys.setrecursionlimit(int(1E6))
from numpy import *

os.chdir("D:/dropbox/Dropbox/rosalind/lcsq")
dat = open("rosalind_lcsq.txt").readlines()
dat = [x.rstrip("\n") for x in dat]

X = dat[0]; Y = dat[1]

def LCSLength(X, Y):
    m = len(X); n = len(Y)
    C = zeros( (m+1, n+1) )
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                C[i+1, j+1] = C[i,j] + 1
            else:
                C[i+1,j+1] = max( C[i+1,j], C[i,j+1] )
    return C

C = LCSLength(X, Y)
print( C )

def backtrack( C, X, Y, i, j):
    if i < 0 or j < 0:
        return ""
    elif X[i] == Y[j]:
        return backtrack(C, X, Y, i-1, j-1) + X[i]
    else:
        if C[i+1,j] > C[i,j+1]:
            return backtrack(C, X, Y, i, j-1)
        else:
            return backtrack(C, X, Y, i-1, j)

print( backtrack(C, X, Y, len(X)-1, len(Y)-1) )