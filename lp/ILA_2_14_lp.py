# Linear program example from Mark J. Debonis' fantastic book 
# Introduction To Linear Algebra: Computation, Application, and Theory
# Example 2.14 is taken from chapter 2:

# maximize 
#   z := 2x + 3y
# subject to
#   z = 2x + 3y
#   x + y <= 4
#   x + 3y <= 6
#   x,y >= 0 

import gurobipy as gp
from gurobipy import GRB
import numpy as np

try: 

    # create a model
    m = gp.Model("ex2.14")

    # create variables
    x = m.addVar(name="x")
    y = m.addVar(name="y")
    z = m.addVar(name="z")

    # specificy objective function
    m.setObjective(z, GRB.MAXIMIZE)

    # create constraints
    m.addConstr(2*x + 3*y == z)
    m.addConstr(x + y <= 4)
    m.addConstr(x + 3*y <= 6)
    m.addConstr(x >= 0)
    m.addConstr(y >= 0)

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