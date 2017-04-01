def is_prime(x):
	if x <= 1:
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

def primes_upto(x):
	primes = []
	for i in range(2, x + 1):
		if is_prime(i):
			primes.append(i)
	return primes

def comps_upto(x):
	comps = []
	for i in range(2, x):
		if not is_prime(i):
			comps.append(i)
	return comps

def prime_fact(x):
	fact = []
	primes = primes_upto(x)
	i = 0
	while x > 1:
		while x % primes[i] == 0:
			x /= primes[i]
			fact.append(primes[i])
		# unsure if below would improve performance
		# if is_prime(x):
		# 	fact.append(x)
		# 	return fact
		i += 1
	return fact

def even_div(x):
	"""finds the smallest positive number that is
	evenly divisible by all numbers from 1 to x"""
	x_prime = primes_upto(x)
	x_comps = comps_upto(x)
	prod = 1
	for i in x_prime:
		prod *= i
	for i in x_comps:
		for j in x_prime:
			# print i
			# print j
			# print ""
			if i % j == 0:
				i /= j
		if i > 1:
			prod *= i
			x_prime = x_prime + prime_fact(i)
			x_prime.sort()
			# print prime_fact(i)
			# print prod
			# print x_prime
			# print ""
	return prod