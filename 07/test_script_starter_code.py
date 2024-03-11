# Starter code for the interpolation test script, tutorial 7, MATH/CSCI2072U, Ontario Tech U, 2024.
import numpy as np
import matplotlib.pyplot as plt
from interpolate import intpl, P

def f(x):
    return np.exp(x)

cond = np.zeros(12)

for n in range(4, 16): 
    x = np.arange(n+1, dtype=float) 
    y = np.exp(x) 

    a, c = intpl(x, y)

    cond[n-4] = c

    nplot = 1000
    xs = np.linspace(0, float(n), nplot) 
    yf = np.zeros(nplot) 
    yp = np.zeros(nplot)  

    for i in range(nplot):
        yf[i] = f(xs[i])
        yp[i] = P(xs[i], a)

    plt.plot(xs, yf, '-k', label='Actual Function')
    plt.plot(xs, yp, '-r', label='Interpolant, n={}'.format(n))
    plt.legend()
    plt.show()

plt.semilogy(range(4, 16), cond, '-o')
plt.xlabel('Number of Nodes (n)')
plt.ylabel('Condition Number')
plt.title('Condition Number of Vandermonde Matrix vs. Number of Nodes')
plt.show()
