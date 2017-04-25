def next_collatz(x):
	# defines next collatz number
	if x % 2 == 0:
		x /= 2
	else:
		x = 3 * x + 1
	return x

def collatz_len(x):
	# finds the # of collatz terms w/o recursion
	terms = 1
	while x != 1:
		x = next_collatz(x)
		terms += 1
	return terms

'''
Attempt#2
Build a dictionary of numbers and their Collatz chain lens
via recusion.  Still too slow...
Note: Building this dictionary and having to check it seems
way slower than brute force
'''
# chainlen = {1:1, 2:2}

# def re_collatz(x):
# 	#finds the # of collatz terms w/ recursion
# 	global chainlen
	
# 	if set([x]).issubset(set(chainlen.keys())):
# 		return chainlen[x]
# 	else:
# 		chainlen[x] = re_collatz(next_collatz(x)) + 1
# 		return chainlen[x]

# for i in range(3, 1000000):
#  	re_collatz(i)
#  	print i


'''
Attempt#1:
brute force approach...takes too long.
Note: started with range 0 --> inf loop
Starting at range 1, reasonable runtime.
'''
longest = 0
long_start = 0
for i in range(1, 1000000):
	if collatz_len(i) > longest:
		long_start = i
		longest = collatz_len(i)

print long_start