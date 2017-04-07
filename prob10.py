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

def sum_primes(x):
	'''brute force way of finding sum of primes'''
	sum = 2
	for i in range(1, x, 2):
		if is_prime(i):
			sum += i
	return sum