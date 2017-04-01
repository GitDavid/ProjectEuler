def sum_squares(x):
	"""sums the square of all int from 1 to x, inclusive"""
	sum = 0
	for i in range(1, x + 1):
		sum += i ** 2
	return sum

def squares_sum(x):
	"""squares the sum of all int from 1 to x, inclusive"""
	sum = 0
	for i in range(1, x + 1):
		sum += i
	return sum ** 2

def diff(x):
	return squares_sum(x) - sum_squares(x)