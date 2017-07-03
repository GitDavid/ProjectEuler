'''
The math behind the programming

43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

Let s be size of spiral (for s odd)
x_s = smallest term in spiral of size s, e.g:
@ s = 3, x_s = 3
@ s = 5, x_s = 13
@ s = 7, x_s = 31
This follows an arithmetic pattern for s >= 5:
x_s = 5 + 8(floor(s) -1)

Note that the terms in any given ring form an arithmetic series with x_s being
    smallest term, and common difference d = floor(s/2) * 2, e.g.
    @ s = 3, terms are:
    5 = 3 + (1 * 2)
    7 = 3 + (2 * 2)
    9 = 3 + (3 * 2)

sum_ring = sum of diagonals in the sth ring, e.g:
@ s = 3, sum_ring = 3 + 5 + 7 + 9
@ s = 5, sum_ring = 13 + 17 + 21 + 25
@ s = 7, sum_ring = 31 + 27 + 43 + 49
Because the terms at each ring is a geometric series, we can use use:
sum_ring = 4 * x_s + 6 * d

Hence, total of spirals can be found by:
1 + sum_ring, for s = {3, 5, 7, ...}
'''
from math import *

def x(s):
    if s == 1:
        return 1
    elif s == 3:
        return 3
    else:
        return x(s - 2) + 2 + (floor(s / 2) - 1) * 8

def d(s):
    return floor(s / 2) * 2

def sum_ring(x, d):
    return 4 * x + 6 * d

spiral_total = 1 # the middle 1 is not counted as part of any series
for s in range (3, 1002, 2):
    print s, x(s), d(s)
    spiral_total += sum_ring(x(s), d(s))

print spiral_total
