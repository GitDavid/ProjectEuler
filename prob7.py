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

def nth_prime(n):
	"""finds the nth prime number"""
	if n == 1:
		return 2
	i = 2
	p = 3
	while i != n:
		p += 2
		if is_prime(p):
			i += 1
	return p