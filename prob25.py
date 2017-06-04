def Fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		num1 = 1
		num2 = 1
		for i in range(n - 2):
			current = num1 + num2
			num1 = num2
			num2 = current
		return current

i = 1
while(len(str(Fib(i))) != 1000):
	i += 1

print i