# rock-paper-scissors nash equilibrium with linear programming
# Sources :=
# | rock-paper-scissors - USNA
#       (https://www.usna.edu/Users/math/dphillip/sa305.s15/phillips/solutions/rock-paper-scissors.sol.pdf)
# | Lecture 12 Linear Programming: Chapter 11: Game Theory 
#       (https://vanderbei.princeton.edu/307/lectures/lec12_show.pdf)

# This example formulates and solves the following simple MIP model:
# x1 := probability of playing rock
# x2 := probability of playing paper1
# x3 := probability of playing scissors

#  maximize
#        min{x2 - x3, -x1 + x2, x1 - x2}
#  subject to
#        x1 + x2 + x3 = 1
#        x1          >= 0
#        x2          >= 0
#        x3          >= 0

import gurobipy as gp
from gurobipy import GRB
import numpy as np


try: 
    
    A = np.array([[0, -1, 1], \
                [1, 0, -1], \
                [-1, 1, 0]]) # this is the payoff matrix of rps
    num_actions = A.shape[0]
    e = np.ones((num_actions, 1)) # vector of all ones

    # e : (3,1) 
    # A : (3,3)
    # v : (1,)
    # x : (3,)
    # create a new model
    m = gp.Model("rps")

    # create variables
    x = m.addMVar(3, lb=None, ub=1.0, name="strategy")
    v = m.addMVar(1, name="value")

    # create objective
    m.setObjective(v, GRB.MAXIMIZE)

    # add constraints
    m.addConstr(e @ v - A @ x <= 0)
    m.addConstr(e.T @ x == 1, "c1")
    #m.addConstrs(x[i] >= 0 for i in range(num_actions))
    # even though lower bound is none and the above constraint is not active, 
    # the solver still gets a positive probability distribution [1/3, 1/3, 1/3]

    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % m.ObjVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')