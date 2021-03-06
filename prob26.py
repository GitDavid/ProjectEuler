from decimal import *
from euler import *

n = 1000
getcontext().prec = 2 * n #set decimal precision to this b/c n-1 is longest possible repeat

def recur_len(str):
    if len(str) < n: #to rule out terminating decimals
        return 0
    first = str[0]
    idx = 0
    while str[idx] == '0':
        idx += 1 # for skipping initial repeating 0's
        # print idx
    first_next_idx = str[idx:].index(first) + idx
    # print first_next_idx
    pattern1 = str[:first_next_idx]
    pattern2 = str[first_next_idx: first_next_idx + len(pattern1)]
    # print first, first_next_idx, pattern1, pattern2
    while True:
        try:
            if pattern1 == pattern2:
                return len(pattern1)
            else:
                first_next_idx += str[first_next_idx + 1:].index(first) + 1
                pattern1 = str[:first_next_idx]
                pattern2 = str[first_next_idx: first_next_idx + len(pattern1)]
                # print first, first_next_idx, pattern1, pattern2
        except ValueError:
            return 0

longest_dec = 0
longest_i = 0

primes = [x for x in range(n) if is_prime(x)]

# print primes

for i in primes:
    # print i
    reciprocal = str(Decimal(1) / Decimal(i))
    # print i, recur_len(reciprocal[2:])
    if recur_len(reciprocal[2:]) > longest_dec:
        longest_dec = recur_len(reciprocal[2:])
        longest_i = i

print longest_i
