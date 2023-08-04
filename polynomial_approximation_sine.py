"""Date: 04/08/2023
   Author: Ashe Vazquez
This program uses gradient descent to find an n-degree polynomial which approximates the sine function between -3 and
3."""

from sympy import *


def calculate_gradient(expr, vars, point):
    """returns the gradient (vector size len(vars)) of the given expression at the given point. point is
    a list. of length len(vars) representing a point in len(vars) dimensional space."""
    grad = []
    for var in range(len(vars)+1):
        grad.append(diff(expr, var).subs(point))
    return grad


def grad_descent_algorithm(expr, vars, point, learning_rate, runs):
    runs += 1
    if runs > 100:
        return point
    gradient_at_point = calculate_gradient(expr, vars, point)
    next_point = point + learning_rate*gradient_at_point #
    grad_descent_algorithm(expr, vars, next_point, learning_rate, runs)


string_polynomial = ""  # string object

x = Symbol('x')
vars = {}
deg = 5  # degree of our polynomial
for i in range(deg+1):
    vars[i] = Symbol('a_'+str(i))
    string_polynomial += "+" + str(vars[i])+"*x**"+str(i)
expr = sympify(string_polynomial)  # finished polynomial expression

# this expression, when evaluated for specific values for a_0, ..., a_5, will return a real number which is what this
# program is trying to minimize.
#testing aaaa
summary_function = integrate((expr - sin(x))**2, (x, -3, 3))

# point = random shit

grad_descent_algorithm(summary_function, vars,)


# vars is a dictionary containing variable names a_0, a_1, ...., a_5 as keys for values 0, 1, ..., 5