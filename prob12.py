# Atempt # 2...use tau

def is_prime(x):
	if x == 1:
		return False
	elif x == 2:
		return True
	else:
		i = 2
		while i**2 <= x:
			if x % i == 0 :
				return False
			i += 1
		return True

def tau(x):
	div = 1
	p = 3
	count = 0
	while x % 2 == 0:
		x /= 2
		count += 1
	if count > 0:
		div *= (count + 1)
	while x != 1:
		count = 0
		if is_prime(p):
			while x % p == 0:
				x /= p
				count += 1
			if count > 0:
				div *= (count + 1)
		p += 2
	return div

# Attempt #1...takes too long to calculate

def nth_trinum(n):
	sum = n * (n + 1) / 2
	return sum

# def find_divisors(x):
# 	div = []
# 	for i in range(1, x + 1):
# 		if x % i == 0:
# 			div.append(i)
# 	return div

# i = 2
# while len(find_divisors(nth_trinum(i))) < 500:
# 	print len(find_divisors(nth_trinum(i)))
# 	i += 2

i = 3
while tau(nth_trinum(i)) < 500:
	# print tau(nth_trinum(i))
	i += 1

print(nth_trinum(i))