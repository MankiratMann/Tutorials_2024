# Author: L. van Veen, UOIT, 2024
# Starter code for the script of tutorial 5.
import numpy as np
import time
import matplotlib.pyplot as plt
import scipy

# Function to create an n x n matrix with band width b.
def create_banded(n, b):
    A = np.zeros((n, n))
    d1 = np.random.rand(n)
    for i in range(n):
        A[i, i] = d1[i]
    for i in range(1, b + 1):
        d1 = np.random.rand(n - i)
        d2 = np.random.rand(n - i)
        for j in range(n - i):
            A[j + i, j] = d1[j]
            A[j, j + i] = d2[j]
    return A

# Test LU decomposition and measure wall time
nstart = 3
nend = 10
ntest = nend - nstart + 1
wtnb = np.zeros((ntest, 2))

for q in range(nstart, nend + 1):
    n = 2**q
    b = 3
    A = create_banded(n, b)
    start = time.time()
    L, U = LUb(A, b)
    elapsed = time.time() - start
    wtnb[q - nstart] = [n, elapsed]

# Plot wall times
plt.loglog(wtnb[:, 0], wtnb[:, 1], label='LU Decomposition')
plt.xlabel('Matrix size')
plt.ylabel('Wall time for sparse LU decomposition (s)')
plt.title('Order n')
plt.legend()
plt.show()
