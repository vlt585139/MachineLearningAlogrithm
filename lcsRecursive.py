"""@author: Victor
    DAT158: Algorithms and Data Structures
    Problem 9.a: Recursive Longest Common Subsequence
"""

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

X = "babbabab"
Y = "bbabbaaab"

print("Lengden av den lengste rekka:", lcs(X , Y, len(X), len(Y)))