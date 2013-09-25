total = 0
for i in range (1000,1000000):
	power_digit = 0
	for c in str(i):
		power_digit += pow(int(c),5)
	if (power_digit == i):
		total += i
print total;