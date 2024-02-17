# Speed test: computing the determinant recursively or with LU decomposition.
# Starter code by L van Veen, Ontario Tech U, 2024.
import numpy as np
import time
import matplotlib.pyplot as plt
from deter import deter
from LU import LU

# Consider matrices of size n X n where n=istart .. iend with recursive computation:
istart = 2
iend = 9
wtimerec = np.zeros((iend - istart + 1, 2))

for n in range(istart, iend + 1):
    A = np.random.rand(n, n)
    start = time.time()
    detA = deter(A)
    elapsed = time.time() - start
    print("n=%d wall time=%f det=%e" % (n, elapsed, detA))
    wtimerec[n - istart, 0] = n
    wtimerec[n - istart, 1] = elapsed

# Consider matrices of size n X n where n=istart .. iend with LU decomposition:
istart = 2
iend = 9
wtimeLU = np.zeros((iend - istart + 1, 2))

for n in range(istart, iend + 1):
    A = np.random.rand(n, n)
    start = time.time()
    L, U, ok = LU(A)
    
    if ok == 1:
        detA = np.prod(np.diag(U))
        elapsed = time.time() - start
        print("n=%d wall time=%f det=%e" % (n, elapsed, detA))
        wtimeLU[n - istart, 0] = n
        wtimeLU[n - istart, 1] = elapsed
    else:
        print("Near-zero pivot in LU decomposition for n=%d\n" % (n))

plt.loglog(wtimerec[:, 0], wtimerec[:, 1], '-*r', label='recursive')
plt.loglog(wtimeLU[:, 0], wtimeLU[:, 1], '-*g', label='using LUP')
plt.loglog(wtimeLU[:, 0], 1e-6 * wtimeLU[:, 0] ** 3, '-k', label='n^3')
plt.legend()
plt.show()