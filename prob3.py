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

def LPF(x):
	ans = 1
	i = 1
	while i**2 <= x:
		if x % i == 0 and is_prime(i):
			ans = i
		if x % i == 0 and (x / i) > ans and is_prime(x / i):
			ans = x / i
		i += 1
	return ans
