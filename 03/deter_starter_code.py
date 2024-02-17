# Recursive computation of the determinant starter code. Tutorial 3 of MATH/CSCI2072 CSI, Ontario Tech U, 2024.
import numpy as np

def deter(A):
    n = A.shape[0]
    
    if n == 2:
        detA = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    else:
        detA = 0.0
        for i in range(n):
            B = np.delete(A, i, axis=0)
            B = np.delete(B, 0, axis=1)
            detA += (-1) ** (i + 1) * A[i, 0] * deter(B)
    return detA