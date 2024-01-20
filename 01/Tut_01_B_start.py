import numpy as np

def F(x, a):
    return x**2 - a

def bisection(a0, b0, k_max, eps_x, eps_f):
    a = a0
    b = b0
    for k in range(k_max):
        c = (a + b) / 2
        f_c = F(c, a)
        print(f'Iteration {k + 1}: x = {c}, F(x) = {f_c}')
        
        if abs(b - a) < eps_x or abs(f_c) < eps_f:
            print(f'Terminated at iteration {k + 1} due to convergence.')
            break
        
        if F(a, a) * F(c, a) < 0:
            b = c
        else:
            a = c

bisection(2, 3, 10, 1e-8, 1e-8)
