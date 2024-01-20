import numpy as np

def phi(x, a):
    return 0.5 * (x + a / x)

def iterate_phi(x0, a, k_max):
    x = x0
    for k in range(k_max):
        x = phi(x, a)
        print(f'Iteration {k + 1}: x = {x}')

def iterate_phi_terminate(x0, a, k_max, epsilon):
    x = x0
    for k in range(k_max):
        x_next = phi(x, a)
        print(f'Iteration {k + 1}: x = {x_next}')
        if abs(x_next - x) < epsilon:
            print(f'Terminated at iteration {k + 1} due to convergence.')
            break
        x = x_next

iterate_phi_terminate(3, 5, 10, 1e-8)
