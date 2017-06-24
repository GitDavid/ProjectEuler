import math
from euler import *

max_b = 0
max_c = 0
max_primes = 0

for i in range(-999, 1000, 2):
	for j in range (-999, 1000, 2):
	    if is_prime(j):
    		x = 0
    		while is_prime(quadratic(1, i, j, x)):
    			x += 1
    		if x > max_primes:
    			max_primes = x
    			max_b = i
    			max_c = j
    			print max_b, max_c, max_primes

print max_b, max_c, max_primes
print max_b * max_c