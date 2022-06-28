# Linear Program used to calculate the best response (strategy) to an opponent's fixed strategy
# Sources :=
# | Safe Opponent Exploitation by SAM GANZFRIED and TUOMAS SANDHOLM
#       (https://vanderbei.princeton.edu/307/lectures/lec12_show.pdf)
# | Fast Algorithms for Finding Randomized Strategies in Game Trees by Daphne Koller
#       (https://vanderbei.princeton.edu/307/lectures/lec12_show.pdf)

# x1 := probability of playing rock
# x2 := probability of playing paper1
# x3 := probability of playing scissors

#  minimize
#        y,v in e.T @ v
#  subject to
#        -Ay + E.Tv  >= 0
#        -Fy         == -f
#        y           >= 0

import gurobipy as gp
from gurobipy import GRB
import numpy as np

try: 
    
    # A is the payoff matrix for rock-paper-scissors
    A : np.ndarray = np.array([[0, -1, 1], \
                [1, 0, -1], \
                [-1, 1, 0]])
    num_actions : int = A.shape[0] # gets the amount of rows you can choose from
    
    # y will be the fixed opponent strategy 
    x = np.array([.9,0.,0.1]) # [0 1 0] plays paper 100% of the time

    F = np.ones((1, num_actions)) # vector of all ones
    f = np.array([1])

    # A : (3,3)
    # y : (3,)
    # x : (3,)
    # F : (3,)
    # f : [1]

    # create a new model
    m = gp.Model("br")

    # create variables
    v = m.addMVar(1)

    # create objective
    m.setObjective(v @ f, GRB.MINIMIZE)

    # add constraints
    m.addConstr(F.T @ v >= -A @ x.T)

    m.optimize()

    print(f"\n\t\t\t     R   P   S")
    print(f"player 1 playing strategy: {x}")
    print(f"value v of best response: {v.X}")

    print(f"Obj(ective) value: {m.ObjVal}")

except gp.GurobiError as e:
    print(f"Error code {e.errno}: {e}")

except AttributeError:
    print('Encountered an attribute error')
