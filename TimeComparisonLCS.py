"""@author: Victor
    DAT158: Algorithms and Data Structures
    Problem 9.c: Time Comparison Longest Common Subsequence
"""

import time

# Recursive LCS
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));   

# Dynamic LCS
def lcsDynamic(X, Y):
 
    m = len(X)
    n = len(Y)
 
    L = [[None]*(n+1) for i in range(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
 
            if i == 0 or j == 0:
                L[i][j] = 0
 
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
 
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    return L[m][n]  # Returnerer lengden på den lengste rekka

X = "We have an algorithm"
Y = "We have two versions"
print("Length of X String: ", len(X))
print("Length of Y String: ", len(Y))

# Recursive LCS
startRec = time.time()
print("Recursive LCS: ", lcs(X , Y, len(X), len(Y)))
endRec = time.time()
print("Time with recursive programming: ", endRec - startRec)

# Dynamic LCS
startDyn = time.time()
print("Dynamic LCS: ", lcsDynamic(X, Y))
endDyn = time.time()
print("Time with dynamic programming: ", endDyn - startDyn)