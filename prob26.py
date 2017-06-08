from decimal import *

#fix recur_len so that it checks for the case where repeating starts after the first char

def recur_len(str):
    first = str[0]
    first_next_idx = str[1:].index(first) + 1
    pattern1 = str[:first_next_idx]
    pattern2 = str[first_next_idx: first_next_idx + len(pattern1)]
    print first, first_next_idx, pattern1, pattern2
    while True:
        try:
            if pattern1 == pattern2:
                return len(pattern1)
            else:
                first_next_idx += str[first_next_idx + 1:].index(first) + 1
                pattern2 = str[first_next_idx: first_next_idx + len(pattern1)]
                print first, first_next_idx, pattern1, pattern2
        except ValueError:
            return 0

longest = 0
for i in range(2, 1001):
    print i
    reciprocal = str(Decimal(1) / Decimal(i))
    if len(reciprocal) <= 5 || recur_len(reciprocal[2:0] == 0):
        pass
    else:
        if recur_len(reciprocal[2:]) > longest:
            longest = i

print longest
