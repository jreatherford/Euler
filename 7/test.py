def isPrime(num):
	if (num == 0) or (num == 1):
		return True
	elif (num%2 == 0):
		return False
	else:
		for x in range(3, ((num/2)-1), 2):
			if num%x == 0:
				return False
	return True


n = 1
primes = 0


while (primes != 10001):
	n = n + 1
	if (isPrime(n) == True):
		primes = primes + 1
	

print n