import numpy as np
import matplotlib.pyplot as plt
from dist import dist          # Function from the cannonball problem (lec 3).
from bisect import bisect      # Simple implementation of bisection.
# from secant import secant    # Write this one yourself!

# Set the parameters:
c = 0.001  # Coefficient of drag.
v0 = 40    # Initial speed of the cannonball.
g = 9.81   # Acceleration of gravity in SI units.
R = 100    # Distance to the target in meters.

# Try to solve for a zero of this function:
def f(x):
    return dist(x, c, g, v0) - R

# Plot first to get an idea of a good initialization of our iterative methods:
xs = np.linspace(0, np.pi/2, 100)
ys = np.zeros((100, 1))
for i in range(0, 100):
    ys[i] = f(xs[i])

plt.plot(xs, ys)
plt.xlabel('Angle of Inclination (radians)')
plt.ylabel('Function Value')
plt.title('Cannon Ball Problem')
plt.show()

# Initial left and right boundary:
a = 0.2
b = 1.0
print('Setting a=%f and b=%f to start bisection...' % (a, b))

# Max number of iterations and target error and residual:
kMax = 100
tolX = 1e-6
tolF = 1e-6

x, recordB = bisect(f, a, b, kMax, tolX, tolF)

# Secant method implementation:
def secant(func, x0, x1, kMax, tolX, tolF):
    record = np.zeros((kMax, 3))
    x_prev, x_curr = x0, x1

    for k in range(kMax):
        f_prev, f_curr = func(x_prev), func(x_curr)
        dfdx = (f_curr - f_prev) / (x_curr - x_prev)

        x_next = x_curr - f_curr / dfdx

        error = np.abs(x_next - x_curr)
        residual = np.abs(f_curr)

        record[k, :] = [k + 1, error, residual]

        if error < tolX or residual < tolF:
            break

        x_prev, x_curr = x_curr, x_next

    return x_curr, record

# Find two initial guesses from the graph created in part (a):
guess1 = 0.3
guess2 = 0.9
print('Setting x0=%f and x1=%f to seed secant iteration...' % (guess1, guess2))

kMax = 100

# Make sure your secant function returns the errors and residuals in the same format as the bisection function!
x_secant, recordS = secant(f, guess1, guess2, kMax, tolX, tolF)

# Plotting the results:
plt.semilogy(recordB[:, 0], recordB[:, 1], 'o', label='Bisection')
plt.semilogy(recordS[:, 0], recordS[:, 1], 'o', label='Secant')
plt.xlabel('Number of Iterations')
plt.ylabel('Error')
plt.title('Error vs. Number of Iterations')
plt.legend()
plt.show()

plt.semilogy(recordB[:, 0], recordB[:, 2], 'o', label='Bisection')
plt.semilogy(recordS[:, 0], recordS[:, 2], 'o', label='Secant')
plt.xlabel('Number of Iterations')
plt.ylabel('Residual')
plt.title('Residual vs. Number of Iterations')
plt.legend()
plt.show()