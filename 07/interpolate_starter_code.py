import numpy as np

def intpl(x, y):
    n = len(x) - 1
    V = np.vander(x, increasing=True)
    c = np.linalg.cond(V, 2)
    a = np.linalg.solve(V, y)
    return a, c
