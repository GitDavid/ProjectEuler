def Fib(n):
	if n <= 3:
		return n
	else: 
		return Fib(n - 1) + Fib(n - 2)

def Fib_even_sum(max):
	i = 2
	sum = 0
	while Fib(i) < max:
		if Fib(i) % 2 == 0:
			sum += Fib(i)
		i += 1
	return sum
