# Author: L. van Veen, UOIT, 2024.
# Starter code for LU decomposition without pivoting for matrix with bandwidth b.
import numpy as np

def LUb(A, b):
    small = 1e-10   # Minimum absolute value of pivot
    n = A.shape[0]  # Extract number of rows
    U = np.copy(A)  # Initialization
    L = np.eye(n)   # Identity matrix for L

    for j in range(1, n):  # Loop over pivots
        for i in range(j + 1, min(j + b + 1, n + 1)):  # Loop over nonzero elements below pivot
            L[i - 1, j - 1] = U[i - 1, j - 1] / U[j - 1, j - 1]  # Compute multiplier
            if abs(U[j - 1, j - 1]) < small:  # Warn if pivot is close to zero
                print("Near-zero pivot element!")
            for k in range(j, n):  # Gauss elimination of nonzero elements on this row
                U[i - 1, k - 1] = U[i - 1, k - 1] - L[i - 1, j - 1] * U[j - 1, k - 1]

    return L, U
