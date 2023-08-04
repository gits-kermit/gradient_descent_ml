"""Date: 04/08/2023
   Author: Ashe Vazquez
This program uses gradient descent to find an n-degree polynomial which approximates the sine function between -3 and
3."""

from sympy import *

def grad_descent_algorithm(expr, vars, point, learning_rate, runs):
    if runs > 100:
        return point
    gradient = diff(expr, (* for * in vars.values()))
    point = point + learning_rate*diff

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

summary_function = integrate((expr - sin(x))**2, (x, -3, 3))




# vars is a dictionary containing variable names a_0, a_1, ...., a_5 as keys for values 0, 1, ..., 5