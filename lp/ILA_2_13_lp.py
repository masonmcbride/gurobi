# Linear program example from Mark J. Debonis' fantastic book 
# Introduction To Linear Algebra: Computation, Application, and Theory
# Example 2.13 is taken from chapter 2:
"""
The college cafeteria is offering a lunch consisting of two entrees. 
The first entree contains 16g of fat, 20g of carbohydrates and 15g of protein per unit serving, 
while the second contains 10g of fat, 30g of carbohydrates and 17g of protein per unit serving. 
For lunch, Harry must have at least 100g of protein, 
but at most 50g of fat and exactly 75g of carbohydrates. 
The first entree costs $ 0.45 per serving 
while the second costs $ 0.65 per serving. 
How many servings of each entree should Harry take so as to meet his nutritional needs 
and spend the least amount of money
"""

# maximize 
#   z := 0.45x1 + 0.65x2
# subject to
#   z = 0.45x1 + 0.65x2
#   15x1 + 17x2 >= 100g of protein
#   16x1 + 10x2 <= 50g of fat
#   20x1 + 30x2 == 75g of carbs
#   xi >= 0 for i in [1,2]

import gurobipy as gp
from gurobipy import GRB
import numpy as np

try: 

    # create a model
    m = gp.Model("ex2.13")

    # create variables
    x1 = m.addVar(name="entree1")
    x2 = m.addVar(name="entree2")
    z = m.addVar(name="value")

    # specificy objective function
    m.setObjective(z, GRB.MAXIMIZE)

    # create constraints
    m.addConstr(0.45*x1 + 0.65*x2 == z)
    m.addConstr(15*x1 + 17*x2 >= 100)
    m.addConstr(16*x1 + 10*x2 <= 150)
    m.addConstr(20*x1 + 30*x2 == 75)
    m.addConstr(x1 >= 0)
    m.addConstr(x2 >= 0)

    # optimize model 
    m.optimize()

    # print results
    for v in m.getVars():
        print(f"{v.VarName} {v.X}")

    print(f"Obj: {m.ObjVal}")


except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')