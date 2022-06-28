# Linear Program formulation of three-card Kuhn Poker
"""
Payoff matrix is generated by traversing the kuhn poker game tree 
because each sequence of moves is uniquely determined by the traversal sequence
the resulting payoff matrix will be sparse, so the LP will use a scipy.sparse array

After the LP has found the optimal solution, the resulting stategy can be generated
by reversing the above process
"""
