''' 
Thinking of each edge as a binary value (right or down)
In a 20x20 grid, we have 20 * 2 values
Since we go from top left to bottom right,
there must be exactly 20 of each binary value
==> Permutation with repetition

'''

import math

print math.factorial(20 * 2) / (math.factorial(20) ** 2)