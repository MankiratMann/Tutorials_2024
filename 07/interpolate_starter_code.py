import numpy as np

def intpl(x, y):
    n = len(x) - 1  # Extract the polynomial order of interpolation.
    V = np.vander(x, increasing=True)  # Vandermonde matrix.
    c = np.linalg.cond(V, 2)  # Condition number of V.
    a = np.linalg.solve(V, y)  # Solve for the coefficients.
    return a, c
