# LU decomposition without pivoting.
# Input: n X n matrix A.
# Output: n X n matrices L and U such that LU=A and L and U are triangular.
import numpy as np

def LU(A):
    ok = 1
    small = 1e-12
    n = np.shape(A)[0]
    U = np.copy(A)
    L = np.identity(n)
    
    for j in range(1, n):
        for i in range(j + 1, n + 1):
            if abs(U[j - 1, j - 1]) < small:
                print("Near-zero pivot!")
                ok = 0
                break
            L[i - 1, j - 1] = U[i - 1, j - 1] / U[j - 1, j - 1]
            for k in range(j, n + 1):
                U[i - 1, k - 1] = U[i - 1, k - 1] - L[i - 1, j - 1] * U[j - 1, k - 1]
    return L, U, ok