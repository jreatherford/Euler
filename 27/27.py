
import math;
#find all the primes you need first;
def build_Primes_Table (size):
	table = [True] * (size + 1);

	for x in range (2, (size + 1)):
		if (table[x] == True):
			for y in range (2*x, (size + 1), x):
				table[y] = False;
	return table;

primes = build_Primes_Table (100000);

bigA = 0;
bigB = 0;
mostPrimes = 0;

for a in range (-1000, 1000):
	for b in range ((-1000 + (a%2)), 1000, 2):
		total = 0;
		n = 0;
		#this only finds primes if a + b is even
		while  (primes[int(math.fabs(((n*n) + (a*n) + b)))] == True):
			n += 1;
			total += 1;
		if (total > mostPrimes):
			bigA = a;
			bigB = b;
			mostPrimes = total;

print (bigA * bigB);