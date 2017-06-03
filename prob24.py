from itertools import permutations

perms = [''.join(p) for p in permutations('0123456789')]
perms.sort()

print perms[999999]