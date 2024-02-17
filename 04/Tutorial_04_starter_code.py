import numpy
import numpy.linalg
import matplotlib.pyplot as plt
import scipy.linalg

smin = 2
smax = 10
rrs = numpy.ones(smax - smin + 1)
res = numpy.ones(smax - smin + 1)
mes = numpy.ones(smax - smin + 1)

for n in range(smin, smax + 1):
    xe = numpy.zeros(n)
    xe[0] = 1

    A = numpy.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            A[i - 1, j - 1] = ((-1) ** (i + j)) / (i + 2 * j)

    r = A[:, 0]
    lu, piv = scipy.linalg.lu_factor(A)
    x = scipy.linalg.lu_solve((lu, piv), r)

    rrs[n - smin] = numpy.linalg.norm(A @ x - r) / numpy.linalg.norm(r)
    res[n - smin] = numpy.linalg.norm(x - xe) / numpy.linalg.norm(xe)
    mes[n - smin] = numpy.linalg.cond(A, p=numpy.inf) * numpy.finfo(float).eps

plt.semilogy(range(smin, smax + 1), res, '-b', range(smin, smax + 1), mes, '-r')
plt.xlim([smin, smax])
plt.xlabel('matrix size')
plt.ylabel('(maximal) relative error')
plt.title('Maximal (red) and actual (blue) relative error')
plt.show()
