def sum35(int):
	ans = 0
	for i in range(int):
		if (i % 3 == 0) or (i % 5 == 0):
			ans += i
	return ans