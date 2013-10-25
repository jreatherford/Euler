def isPandigital (num):
	num = sorted(str(num))
	for i in range (0,len(num)):
		if (i + 1 != int(num[i])):
			return False
	return True;


def findPrimes(size, prime_table):
    primes = []
    for i in range (2, size + 1):
        if prime_table[i] == True:
            primes.append(i)
            for j in range (2*i, size + 1, i):
                prime_table [j] = False
    return primes

size = 7654321
prime_table = [True] * (size + 1)
prime_table[1] = False
primes = findPrimes(size, prime_table)

max = 0;
for i in primes:
	if isPandigital(i):
		if i > max:
			max = i

print max